package stdlib
import (
    "time"
    "list"
)

// Specify tariff format
// https://cuelang.org/docs/concept/how-cue-enables-data-validation/
// https://cuelang.org/docs/concept/how-cue-works-with-yaml/

#MGA: =~"^50Y[A-Z0-9-]{10}"
#GLN: =~"^7080[0-9]{9}$"

#Selskap: {
    netteier!: string
    gln!: [...#GLN]
    sist_oppdatert!: time.Format(time.RFC3339Date)
    kilder!: list.MinItems(1)
    tariffer!: [...#Tariff]
}

#Tariff: {
    gyldig_fra!: time.Format(time.RFC3339Date)
    gyldig_til?: time.Format(time.RFC3339Date)
    id!: =~ "^[a-zæøå0-9-]+$"
    navn?: string
    kommentar?: string
    kundegruppe!: "husholdning" | "hytte" | "privat"
    mga?: [...#MGA]
    energiledd!: #Energiledd
    fastledd!: #Fastledd
}

#Energiledd: {
    grunnpris!: float | int
    unntak?: [...#Unntak]
}

#Unntak: {
    navn!: string
    // TODO riktig format på timer
    timer?: string
    dager?: [...#Dag]
    måneder?: [...#Måned]
    pris!: float | int
}

#Dag: "mandag" | "tirsdag" | "onsdag" | "torsdag" | "fredag" | "lørdag" | "søndag" | "ukedag" | "helg" | "helligdager" | "fridag" | "virkedag" | "alle"
#Måned: "januar" | "februar" | "mars" | "april" | "mai" | "juni" | "juli" | "august" | "september" | "oktober" | "november" | "desember"

#Fastledd: {
    metode!: "TRE_DØGNMAX_MND" | "FEM_VEKTET_ÅR" | "OV_TREFASE" | "MND_MAX" | "UKJENT"
    terskel_inkludert!: bool | null
    terskler!: [...#Terskel]
}

#Terskel: {
    terskel: int
    pris!: float | int
}
