#!/usr/bin/env python3
import argparse
import datetime
import yaml
import zoneinfo

def parse_args():
    parser = argparse.ArgumentParser(description='Print hours between two dates')
    parser.add_argument('--fra', help='Start date in ISO format (YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('--til', help='End date in ISO format (YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('--tariff', help='File name to print')
    return parser.parse_args()

def load_tariff(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

def hours(range_str):
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

    print(args.tariff)

    tariff = load_tariff(args.tariff)
    print(yaml.dump(tariff))

    # TODO not just pick the first one and actuall deal with all unntak
    # TODO deal with dates and consumer types etc
    base_price = tariff['tariffer'][0]['energiledd']['grunnpris']
    alt_price = tariff['tariffer'][0]['energiledd']['unntak'][0]['pris']
    alt_hours = hours(tariff['tariffer'][0]['energiledd']['unntak'][0]['timer'])


    current_date = from_date_utc
    while current_date < to_date_utc:

        hour_osl = current_date.astimezone(OSL)
        hour = int(hour_osl.strftime('%H'))

        price = base_price
        if hour in alt_hours:
            price = alt_price

        print(f"{hour_osl.strftime('%Y-%m-%d %H:00%z')} - {hour:02d} - {price}")

        current_date += datetime.timedelta(hours=1)

if __name__ == '__main__':
    main()
