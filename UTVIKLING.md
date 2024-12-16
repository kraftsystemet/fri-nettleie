# Utvikling

Denne fila er for deg som ønsker å bidra teknisk eller med kode til
fri-nettleie.

> [!TIP]
> Generelt er det lurt å åpne/kommentere på et issue før du går igang med noe.
>
> Sjekk issues her på GitHub.

## Språk

Vi skripter med python og bash. I begynnelsen skrev vi endel av skriptene med
iblandet norsk språk. Vi forsøker å jobber oss ut av det. Data, beskrivelser og
tariffer er på norsk, men koden skal være på engelsk.

## Endringsmonitorering

Vi bruker [changedetection](https://github.com/dgtlmoon/changedetection.io) for
å monitorere endringer. Enn så lenge kjører vi vi lokalt med docker. For å komme
igang, kjør følgende

```bash
make changedetection
make kilder
```

Dette starter changedetection lokalt med docker compose og dytter inn alle
url'er fra `kilder` i tariffene. Se changedetection på
[localhost:5000](http://localhost:5000).
