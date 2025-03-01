import yaml
import polars as pl
from typing import List, Optional
from datetime import datetime

class Terskel:
    def __init__(self, terskel: int, pris: float):
        self.terskel = terskel
        self.pris = pris

    def __repr__(self):
        return f"Terskel(terskel={self.terskel}, pris={self.pris})"

class Unntak:
    def __init__(self, navn: str, pris: float, måneder: Optional[List[str]] = None, dager: Optional[List[str]] = None, timer: Optional[str] = ""):
        self.navn = navn
        self.timer = timer
        self.pris = pris
        self.måneder = måneder or []
        self.dager = dager or []

    def __repr__(self):
        return f"Unntak(navn={self.navn}, timer={self.timer}, pris={self.pris}, måneder={self.måneder})"

class Fastledd:
    def __init__(self, metode: str, terskel_inkludert: bool, terskler: List[Terskel]):
        self.metode = metode
        self.terskel_inkludert = terskel_inkludert
        self.terskler = terskler

    def __repr__(self):
        return f"Fastledd(metode={self.metode}, terskler={self.terskler})"

class Energiledd:
    def __init__(self, grunnpris: float, unntak: List[Unntak]):
        self.grunnpris = grunnpris
        self.unntak = unntak

    def __repr__(self):
        return f"Energiledd(grunnpris={self.grunnpris}, unntak={self.unntak})"

class Tariff:
    def __init__(self, kundegruppe: str, fastledd: Fastledd, energiledd: Energiledd, gyldig_fra: str):
        self.kundegruppe = kundegruppe
        self.fastledd = fastledd
        self.energiledd = energiledd
        self.gyldig_fra = gyldig_fra

    def __repr__(self):
        return f"Tariff(kundegruppe={self.kundegruppe}, fastledd={self.fastledd}, energiledd={self.energiledd}, gyldig_fra={self.gyldig_fra})"

class Nettariff:
    def __init__(self, netteier: str, gln: List[str], sist_oppdatert: str, kilder: List[str], tariffer: List[Tariff]):
        self.netteier = netteier
        self.gln = gln
        self.sist_oppdatert = sist_oppdatert
        self.kilder = kilder
        self.tariffer = tariffer

    def get_summary(self):
        """Returns a summary of the grid tariff"""
        summary = []
        for tariff in self.tariffer:
            min_fastledd = min(t.pris for t in tariff.fastledd.terskler)
            max_fastledd = max(t.pris for t in tariff.fastledd.terskler)
            grunnpris = tariff.energiledd.grunnpris
            antall_terskler = len(tariff.fastledd.terskler)
            antall_unntak = len(tariff.energiledd.unntak)
            summary.append({
                "kundegruppe": tariff.kundegruppe,
                "gyldig_fra": tariff.gyldig_fra,
                "min_fastledd": min_fastledd,
                "max_fastledd": max_fastledd,
                "grunnpris": grunnpris,
                "antall_terskler": antall_terskler,
                "antall_unntak": antall_unntak
            })
        return summary

    def get_exceptions(self) -> List[str]:
        return [u.navn for t in self.tariffer for u in t.energiledd.unntak]
    
    def get_tariffs_by_kundegruppe(self, kundegruppe: str) -> List[Tariff]:
        """
        Return all tariffs for a given customer group (kundegruppe)
        Note: not really usefull as of now.
        """
        return [t for t in self.tariffer if t.kundegruppe == kundegruppe]
    
    def filter_tariffs_by_date(self, date: str) -> List[Tariff]:
        """Return all tariffs that are valid for a given date (YYYY-MM-DD) 
        by checking gyldig_fra and ensuring no newer entry exists."""
        
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        valid_tariffs = []
        for tariff in self.tariffer:
            start_date = datetime.strptime(tariff.gyldig_fra, "%Y-%m-%d").date()

            if start_date <= target_date:
                # check if there is a newer tariff for the same kundegruppe
                newer_tariffs = [
                    t for t in self.tariffer
                    if t.kundegruppe == tariff.kundegruppe and 
                    datetime.strptime(t.gyldig_fra, "%Y-%m-%d").date() > start_date
                ]

                # if no newer tariff exists, it means this is the active one
                if not any(t.gyldig_fra <= date for t in newer_tariffs):
                    valid_tariffs.append(tariff)

        return valid_tariffs
    
    def get_energiledd_for_timestamp(self, timestamp: str, kundegruppe: str = "privat") -> float:
        """
        Returns the price for a given timestamp and customer group
        """
        norsk_måned = {
            "january": "januar", "february": "februar", "march": "mars",
            "april": "april", "may": "mai", "june": "juni",
            "july": "juli", "august": "august", "september": "september",
            "october": "oktober", "november": "november", "december": "desember"
        }

        norsk_ukedag = {
            "monday": "mandag", "tuesday": "tirsdag", "wednesday": "onsdag",
            "thursday": "torsdag", "friday": "fredag", "saturday": "lørdag",
            "sunday": "søndag"
        }
        # har ikke lagt til helligdag, virkedag osv


        # datetime parsing
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
        usage_date = dt.date()
        usage_hour = dt.hour
        usage_minute = dt.minute # will the tariffs be on 15-mins ?? 
        usage_month = norsk_måned[dt.strftime("%B").lower()]
        usage_weekday = norsk_ukedag[dt.strftime("%A").lower()]

        # finding the active tariff for this date
        active_tariff = self.filter_tariffs_by_date(str(usage_date))
        tariff = next((t for t in active_tariff if t.kundegruppe == kundegruppe), None)

        if not tariff:
            raise ValueError(f"No tariff found for {kundegruppe} on {usage_date}")
        
        price = tariff.energiledd.grunnpris

        for unntak in tariff.energiledd.unntak:
            if unntak.måneder and usage_month in unntak.måneder:
                if unntak.timer and usage_hour in range(*map(int, unntak.timer.split("-"))):
                    price = unntak.pris
                    break
        # will add more conditions here for dager, helligdager, virkedager ... 

        return price
    
    def to_polars(self) -> pl.DataFrame:
        """
        Converts the grid tariff to a flattened Polars DataFrame
        Need to figure out what is interesting and how to handle unntak vs terskler.
        Rows increase quickly...
        """

        records = []
        for tariff in self.tariffer:
            for terskel in tariff.fastledd.terskler:
                for unntak in tariff.energiledd.unntak or [{}]:
                    records.append({
                        "netteier": self.netteier,
                        "gln": self.gln,
                        "sist_oppdatert": self.sist_oppdatert,
                        "kundegruppe": tariff.kundegruppe,
                        "gyldig_fra": tariff.gyldig_fra,
                        "fastledd_metode": tariff.fastledd.metode,
                        "fastledd_terskel": terskel.terskel,
                        "fastledd_pris": float(terskel.pris),
                        "energiledd_grunnpris": float(tariff.energiledd.grunnpris),
                        "unntak_navn": unntak.navn if unntak else "",
                    })
        return pl.DataFrame(records)

    def __repr__(self):
        return f"Nettariff(netteier={self.netteier}, tariffer={self.tariffer})"
    
def get_grid_tariff(yaml_file: str) -> Nettariff:
    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    tariffer = []
    for t in data["tariffer"]:
        fastledd = Fastledd(
            metode=t["fastledd"]["metode"],
            terskel_inkludert=t["fastledd"]["terskel_inkludert"],
            terskler=[Terskel(**terskel) for terskel in t["fastledd"]["terskler"]]
        )
        energiledd = Energiledd(
            grunnpris=t["energiledd"]["grunnpris"],
            unntak=[Unntak(**unntak) for unntak in t["energiledd"].get("unntak", [])]
        )
        tariffer.append(Tariff(
            kundegruppe=t["kundegruppe"],
            fastledd=fastledd,
            energiledd=energiledd,
            gyldig_fra=t["gyldig_fra"]
        ))

    return Nettariff(
        netteier=data["netteier"],
        gln=data["gln"],
        sist_oppdatert=data["sist_oppdatert"],
        kilder=data["kilder"],
        tariffer=tariffer
    )
