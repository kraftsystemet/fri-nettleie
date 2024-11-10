import requests
import enum

class Endpoint(enum.Enum):
    Maned = "NettleiePerOmradePrManedHusholdningFritidEffekttariffer"
    Time = "NettleiePerOmradePrTimeHusholdningFritidEffekttariffer"

class TariffGruppe(enum.Enum):
    Husholdning = "Husholdning"
    Hytter = "Hytter og fritidshus"


# https://biapi.nve.no/nettleietariffer/swagger/index.html
TARIFFER_URL="https://biapi.nve.no/nettleietariffer/api/"




def get_konsesjonarer_fylker(dato):

    url = f"{TARIFFER_URL}{Endpoint.Maned.value}"

    headers = {'accept': 'application/json'}
    params = {
        "FraDato": dato,
        "Tariffgruppe": TariffGruppe.Husholdning.value,
        "Kundegruppe" : "2"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # data is a list of
    # {
    #     "datoId": "2024-11-01T00:00:00",
    #     "tariffgruppe": "Husholdning",
    #     "kundegruppe": "Eksempelkunde 4 (sommer)/6 (vinter) kW, 20 000kWh",
    #     "konsesjonar": "LEGA NETT AS",
    #     "organisasjonsnr": "924868759",
    #     "fylkeNr": "56",
    #     "fylke": "Finnmark",
    #     "harMva": false,
    #     "harForbruksavgift": false,
    #     "fastleddEks": 339,
    #     "energileddEks": 17.33,
    #     "effekttrinnFraKw": 5,
    #     "effekttrinnTilKw": 10,
    #     "omregnetPrisEks": 684.9072,
    #     "fastleddInk": 339,
    #     "energileddInk": 17.33,
    #     "omregnetPrisInk": 684.9072,
    #     "omregnetOrekWhEks": 34.556393,
    #     "omregnetOrekWhInk": 34.556393,
    #     "omregnetOrekWhEksFylkessnitt": 41.822567,
    #     "omregnetOrekWhInkFylkessnitt": 41.822567,
    #     "omregnetOrekWhEksLandssnitt": 39.38176,
    #     "omregnetOrekWhInkLandssnitt": 67.46451,
    #     "fylkesvekt": 0.033248,
    #     "landsvekt": 0.000729
    # }

    konsesjonarer = {}
    for k in data:
        org = k["organisasjonsnr"]
        fylke = k["fylkeNr"]

        if org not in konsesjonarer:
            konsesjonarer[org] = []

        if fylke not in konsesjonarer[org]:
            konsesjonarer[org].append(fylke)

    return konsesjonarer

def get_timedata(dato, fylke, org):

    url = f"{TARIFFER_URL}{Endpoint.Time.value}"

    headers = {'accept': 'application/json'}
    params = {
        "ValgtDato": dato,
        "Tariffgruppe": "Husholdning",
        "FylkeNr": fylke,
        "OrganisasjonsNr" : org,
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

def get_oppsummering(dato, fylker, org):

    priser = []
    terskler = {}

    for fylke in fylker:

        data = get_timedata(dato, fylke, org)


        for d in data:
            if d["energileddEks"] not in priser:
                priser.append(d["energileddEks"])

            if d["effekttrinnFraKw"] not in terskler:
                terskler[d["effekttrinnFraKw"]] = d["fastleddEks"]

    return {
        "priser": priser,
        "terskler": [{ "terskel" : t, "pris" : terskler[t]*12} for t in sorted(list(terskler.keys())) ]
    }
