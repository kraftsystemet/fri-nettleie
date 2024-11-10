import holidays
from dataclasses import dataclass
from typing import List
import datetime

HELLIGDAGER = holidays.Norway()

@dataclass
class Unntak:
    timer: List[int]
    pris: float | None
    tillegg: float | None
    dager: List[str]
    mnd: List[str]

    def matcher_dager(self, t: datetime.datetime) -> bool:

        if self.dager == []:
            return True

        if "alle" in self.dager:
            return True

        ukedag = t.weekday()
        ukedag_navn = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"][ukedag]

        if ukedag_navn in self.dager:
            return True

        er_helligdag = t in HELLIGDAGER
        er_helg = ukedag in [5, 6]
        er_fridag = er_helg or er_helligdag
        er_ukedag = ukedag in [0, 1, 2, 3, 4]

        if "ukedag" in self.dager and er_ukedag:
            return True

        if "helg" in self.dager and er_helg:
            return True

        if "helligdager" in self.dager and er_helligdag:
            return True

        if "fridag" in self.dager and er_fridag:
            return True

        if "virkedag" in self.dager and not er_fridag:
            return True

        return False

    def matcher_mnd(self, t: datetime.datetime) -> bool:
        if self.mnd == []:
            return True
        if "alle" in self.mnd:
            return True

        mnd = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"][t.month - 1]
        return mnd in self.mnd

    def matcher_timer(self, t: datetime.datetime) -> bool:
        if self.timer == []:
            return True
        return int(t.strftime('%H')) in self.timer

    def matcher(self, t: datetime.datetime) -> bool:

        return self.matcher_timer(t) and self.matcher_dager(t) and self.matcher_mnd(t)

    def unntakspris(self, grunnpris: float) -> float:
        if self.tillegg is not None:
            return grunnpris + self.tillegg
        return self.pris
