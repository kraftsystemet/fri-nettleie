package stdlib
import (
    "time"
    "list"
)

// Specify tariff format
// https://cuelang.org/docs/concept/how-cue-enables-data-validation/
// https://cuelang.org/docs/concept/how-cue-works-with-yaml/

#Mga: =~"^50Y[A-Z0-9-]{10}"

#Selskap: {
    netteier!: string
    gln!: =~"^7[0-9]{12}$"
    sist_oppdatert!: time.Format(time.RFC3339Date)
    kilder!: list.MinItems(1)
    tariffer!: [...#Tariff]
}

#Tariff: {
    gyldig_fra!: time.Format(time.RFC3339Date)
    gyldig_til?: time.Format(time.RFC3339Date) | null
    id!: =~ "^[a-zæøå0-9-]+$"
    kommentar?: string
    kundegruppe!: "husholdning" | "hytte" | "privat"
    mga?: [...#Mga]
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
    // TODO enten pris eller tillegg
    pris?: float | int | null
    tillegg?: float | int | null
}

#Dag: "mandag" | "tirsdag" | "onsdag" | "torsdag" | "fredag" | "lørdag" | "søndag" | "ukedag" | "helg" | "helligdager" | "fridag" | "virkedag" | "alle"
#Måned: "januar" | "februar" | "mars" | "april" | "mai" | "juni" | "juli" | "august" | "september" | "oktober" | "november" | "desember"

#Fastledd: {
    metode!: "TRE_DØGNMAX_MND" | "FEM_VEKTET_ÅR" | "OV_TREFASE"
    terskel_inkludert!: bool
    terskler!: [...#Terskel]
}

#Terskel: {
    terskel: int
    pris!: float | int
}
