import requests
import enum
import dataclasses
from typing import List


class Endpoint(enum.Enum):
    Maned = "NettleiePerOmradePrManedHusholdningFritidEffekttariffer"
    Time = "NettleiePerOmradePrTimeHusholdningFritidEffekttariffer"


class TariffGruppe(enum.Enum):
    Husholdning = "Husholdning"
    Hytter = "Hytter og fritidshus"


@dataclasses.dataclass
class Konsesjonar:
    org: str
    navn: str
    fylker: List[str]
    fylker_navn: List[str]


# https://biapi.nve.no/nettleietariffer/swagger/index.html
TARIFFER_URL = "https://biapi.nve.no/nettleietariffer/api/"


def get_mnd_data(dato):
    """
    data is a list of
    ```json
    {
        "datoId": "2024-11-01T00:00:00",
        "tariffgruppe": "Husholdning",
        "kundegruppe": "Eksempelkunde 4 (sommer)/6 (vinter) kW, 20 000kWh",
        "konsesjonar": "LEGA NETT AS",
        "organisasjonsnr": "924868759",
        "fylkeNr": "56",
        "fylke": "Finnmark",
        "harMva": false,
        "harForbruksavgift": false,
        "fastleddEks": 339,
        "energileddEks": 17.33,
        "effekttrinnFraKw": 5,
        "effekttrinnTilKw": 10,
        "omregnetPrisEks": 684.9072,
        "fastleddInk": 339,
        "energileddInk": 17.33,
        "omregnetPrisInk": 684.9072,
        "omregnetOrekWhEks": 34.556393,
        "omregnetOrekWhInk": 34.556393,
        "omregnetOrekWhEksFylkessnitt": 41.822567,
        "omregnetOrekWhInkFylkessnitt": 41.822567,
        "omregnetOrekWhEksLandssnitt": 39.38176,
        "omregnetOrekWhInkLandssnitt": 67.46451,
        "fylkesvekt": 0.033248,
        "landsvekt": 0.000729
    }
    ```
    """
    url = f"{TARIFFER_URL}{Endpoint.Maned.value}"

    headers = {"accept": "application/json"}
    params = {
        "FraDato": dato,
        "Tariffgruppe": TariffGruppe.Husholdning.value,
        "Kundegruppe": "2",
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()


def get_consessionares():
    url = "https://nve.geodataonline.no/arcgis/rest/services/Nettanlegg2/MapServer/6/query"
    params = {"where": "1=1", "outFields": "*", "f": "json"}
    response = requests.get(url, params=params)

    data = response.json()
    features = data["features"]

    # Extract attributes from features and sort by NAVN

    # "KONSTYPE": "VANLIG",
    # "NAVN": "SYGNIR AS",
    # "EIER_ID": 924619260,
    # "EIERTYPE": "EVERK",

    consessionares = {}

    for feature in features:
        org = str(feature["attributes"]["EIER_ID"])
        name = feature["attributes"]["NAVN"]

        if org not in consessionares:
            consessionares[org] = name

    return consessionares


def get_konsesjonarer(dato):
    data = get_mnd_data(dato)

    konsesjonarer = {}
    for k in data:
        org = k["organisasjonsnr"]
        navn = k["konsesjonar"].replace("*", "").split("(")[0].strip()

        if org not in konsesjonarer:
            konsesjonarer[org] = Konsesjonar(
                org=org,
                navn=navn,
                fylker=[k["fylkeNr"]],
                fylker_navn=[k["fylke"].strip()],
            )

        if k["fylkeNr"] not in konsesjonarer[org].fylker:
            konsesjonarer[org].fylker.append(k["fylkeNr"])
            konsesjonarer[org].fylker_navn.append(k["fylke"].strip())

    return konsesjonarer


def get_time_data(dato, fylke, org):
    url = f"{TARIFFER_URL}{Endpoint.Time.value}"

    headers = {"accept": "application/json"}
    params = {
        "ValgtDato": dato,
        "Tariffgruppe": "Husholdning",
        "FylkeNr": fylke,
        "OrganisasjonsNr": org,
    }

    response = requests.get(url, headers=headers, params=params)

    # response is a list of
    # {
    #     "datoId": "2024-11-01T00:00:00",
    #     "tariffgruppe": "Husholdning",
    #     "kundegruppe": null,
    #     "konsesjonar": "MIDTNETT AS",
    #     "organisasjonsnr": "917856222",
    #     "fylkeNr": "33",
    #     "fylke": "Buskerud",
    #     "harMva": true,
    #     "harForbruksavgift": true,
    #     "fastleddEks": 2096,
    #     "energileddEks": 32,
    #     "effekttrinnFraKw": 50,
    #     "effekttrinnTilKw": 74.99,
    #     "fastleddInk": 2620,
    #     "energileddInk": 60.55,
    #     "time": 19
    # }

    data = response.json()
    return data


def get_oppsummering(dato, fylker: List[str], org: str):
    priser = []
    terskler = {}

    for fylke in fylker:
        data = get_time_data(dato, fylke, org)

        for d in data:
            if d["energileddEks"] not in priser:
                priser.append(d["energileddEks"])

            if d["effekttrinnFraKw"] not in terskler:
                terskler[d["effekttrinnFraKw"]] = d["fastleddEks"]

    return {
        "priser": priser,
        "terskler": [
            {"terskel": t, "pris": terskler[t] * 12}
            for t in sorted(list(terskler.keys()))
        ],
    }


def get_summary(dates: List[str], counties: List[str], org: str):
    """
    Fetches and summarizes energy tariff data for given dates, counties, and organization.

    Args:
        dates (List[str]): A list of dates for which to fetch the energy data.
        counties (List[str]): A list of county identifiers to fetch the data for.
        org (str): The organization identifier.

    Returns:
        dict: A dictionary containing:
            - "prices": A list of unique energy prices (energileddEks) encountered.
            - "levels": A list of dictionaries, each containing:
                - "levels": The power threshold (effekttrinnFraKw).
                - "price": The corresponding fixed charge (fastleddEks) multiplied by 12.
    """

    prices = []
    levels = {}

    for dt in dates:
        for fylke in counties:
            data = get_time_data(dt, fylke, org)

            for d in data:
                if d["energileddEks"] not in prices:
                    prices.append(d["energileddEks"])

                if d["effekttrinnFraKw"] not in levels:
                    levels[d["effekttrinnFraKw"]] = d["fastleddEks"]

    return {
        "energiledd": sorted(prices),
        "terskler": [
            {"terskel": t, "pris": round(levels[t] * 12, 3)}
            for t in sorted(list(levels.keys()))
        ],
    }
