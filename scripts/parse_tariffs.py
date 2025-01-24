import yaml
from typing import List
import polars as pl

from dataclass_tariffs import TariffYAML, Tariff, Fastledd, Terskel, Energiledd, Unntak

def read_yaml(yaml_path: str) -> dict:
    with open(yaml_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data

def parse_tariffs(yaml_path: str) -> TariffYAML:
    data = read_yaml(yaml_path)

    def parse_unntak(unntak_data):
        return [
            Unntak(
                navn=unntak.get('navn'),
                timer=unntak.get('timer'),
                dager=unntak.get('dager', []),
                pris=unntak.get('pris')
            )
            for unntak in unntak_data
        ]

    def parse_energiledd(data):
        unntak = parse_unntak(data.get('unntak', []))
        return Energiledd(
            grunnpris=data.get('grunnpris'),
            unntak=unntak
        )
    
    def parse_terskel(data):
        return Terskel(
            terskel=data.get('terskel'),
            pris=data.get('pris')
        )
    
    def parse_fastledd(data):
        terskler = [parse_terskel(t) for t in data.get('terskler', [])]
        return Fastledd(
            metode=data.get('metode'),
            terskel_inkludert=data.get('terskel_inkludert'),
            terskler=terskler
        )
    
    def parse_tariff(data):
        return Tariff(
            kundegruppe=data.get('kundegruppe'),
            gyldig_fra=data.get('gyldig_fra'),
            gyldig_til=data.get('gyldig_til'),
            fastledd=parse_fastledd(data.get('fastledd', {})),
            energiledd=parse_energiledd(data.get('energiledd', {}))
        )
    
    tariffer = [parse_tariff(t) for t in data.get('tariffer', [])]
    return TariffYAML(
        netteier=data.get('netteier'),
        gln=data.get('gln'),
        sist_oppdatert=data.get('sist_oppdatert'),
        kilder=data.get('kilder', []),
        tariffer=tariffer
    )

if __name__ == '__main__':
    yaml_path = "./tariffer/hallingdalkraftnett.yml"
    tariff_data = parse_tariffs(yaml_path)
    print(tariff_data)