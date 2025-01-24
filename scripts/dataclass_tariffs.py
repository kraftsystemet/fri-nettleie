from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Unntak:
    navn: str = None
    måneder: Optional[str] = field(default_factory=list)
    dager: Optional[str] = field(default_factory=list)
    timer: str = None
    pris: float = None

@dataclass
class Energiledd:
    grunnpris: float = None
    unntak: Optional[List[Unntak]] = field(default_factory=list)

@dataclass
class Terskel:
    terskel: int = None
    pris: float = None

@dataclass
class Fastledd:
    metode: str = None
    terskel_inkludert: bool = None
    terskler: Optional[List[Terskel]] = field(default_factory=list)

@dataclass
class Tariff:
    kundegruppe: str = None
    gyldig_fra: str = None
    gyldig_til: Optional[str] = None
    fastledd: Fastledd = None
    energiledd: Energiledd = None

@dataclass
class TariffYAML:
    netteier: str = None
    gln: List[str] = None
    sist_oppdatert: str = None
    kilder: Optional[List[str]] = field(default_factory=list)
    tariffer: List[Tariff] = None

