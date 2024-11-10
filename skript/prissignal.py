#!/usr/bin/env python3
import argparse
import datetime
import yaml
import zoneinfo
import os

from nettleie import Unntak

def parse_args():
    parser = argparse.ArgumentParser(description='Print hours between two dates')
    parser.add_argument('--fra', help='Start date in ISO format (YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('--til', help='End date in ISO format (YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('--tariff-fil', help='Innsamlet tariff-fil')
    parser.add_argument('--tariff', help='Tariff-id', default=None)
    return parser.parse_args()

def load_tariff(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

def hours(range_str):
    if range_str == '':
        return []
    start, end = range_str.split('-')
    return list(range(int(start), int(end) + 1))

def main():
    args = parse_args()
    OSL = zoneinfo.ZoneInfo("Europe/Oslo")
    UTC = zoneinfo.ZoneInfo("UTC")
    from_date = datetime.datetime.fromisoformat(args.fra)
    to_date = datetime.datetime.fromisoformat(args.til) + datetime.timedelta(days=1)


    from_date_osl = from_date.astimezone(OSL)
    to_date_osl = to_date.astimezone(OSL)

    from_date_utc = from_date_osl.astimezone(UTC)
    to_date_utc = to_date_osl.astimezone(UTC)

    print(f"TARIFF FIL: {args.tariff_fil}")

    data = load_tariff(args.tariff_fil)

    print("INNSAMLET TARIFF:")
    print("")
    print(yaml.dump(data))

    tariffer = data.get('tariffer')

    tariff = tariffer[0]

    if args.tariff is not None:
        treff = [i for t,i in tariffer if t['id'] == args.tariff]
        if len(treff) == 0:
            print(f"Tariff {args.tariff} ikke funnet")
            os.exit(1)
        tariff = treff[0]

    print(f"TARIFF: {tariff['id']}\n")

    grunnpris = tariff['energiledd']['grunnpris']

    unntak = []

    for u in tariff['energiledd']['unntak']:
        unntak.append(Unntak(
            timer=hours(u.get('timer', '')),
            pris=u.get('pris',None),
            tillegg=u.get('tillegg',None),
            dager=u.get('dager',[]),
            mnd=u.get('måneder',[])
        ))

    print(f"UNNTAK:\n\n{unntak}\n")


    print("PRISER:\n")

    current_date = from_date_utc
    while current_date < to_date_utc:

        t_osl = current_date.astimezone(OSL)
        t_pris = grunnpris

        for u in unntak:
            if u.matcher(t_osl):
                t_pris = u.unntakspris(t_pris)

        print(f"{t_osl.strftime('%Y-%m-%d %H:00%z')} - {t_pris}")

        current_date += datetime.timedelta(hours=1)

if __name__ == '__main__':
    main()
