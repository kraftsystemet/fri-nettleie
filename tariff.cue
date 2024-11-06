package stdlib
import (
    "time"
    "list"
)

// Specify tariff format
// https://cuelang.org/docs/concept/how-cue-works-with-yaml/

#Tariff: {
    gyldig_fra!: time.Format(time.RFC3339Date)
    gyldig_til?: time.Format(time.RFC3339Date) | ""
}

#Selskap: {
    gln!: =~"^7[0-9]{12}$"
    sist_oppdatert!: time.Format(time.RFC3339Date)
    kilder!: list.MinItems(1)
    tariffer!: [...#Tariff]
}
