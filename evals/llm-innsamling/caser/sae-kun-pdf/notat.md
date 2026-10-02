# Sør Aurdal Energi, kilde uten prisdata

Den virkelige teksten fra siden nevner «Tariffer for nettleie per 1.9.2026», men det er bare en lenke
til en PDF. Ingen priser står i teksten. Fastleddmetoden i den eksisterende filen (`MND_MAX`) og
vinterpriser (sesong) gjør at modellen heller ikke kan utlede noe fra forrige periode.

Riktig oppførsel: STOPPET. Modellen skal
- si at prisene står i en PDF som ikke er tilgjengelig som tekst,
- IKKE bruke forrige periodes priser eller en «typisk økning»,
- be brukeren lime inn teksten fra PDF-en «Tariffer for nettleie per 1.9.2026».
