#!/usr/bin/env python3
# Template tariff til HTML

import json
import yaml
import os
from datetime import date, datetime
import dateutil.parser


import os
import yaml
from jinja2 import Template, StrictUndefined, Environment

env = Environment()
env.policies['json.dumps_kwargs']['ensure_ascii'] = False

with open('scripts/templates/netteier.j2.html', 'r') as f:
    template = Template(f.read(),undefined=StrictUndefined)

netteiere = []


# Per netteier
for filename in os.listdir('tariffer'):
    if filename.endswith('.yml'):
        print(filename)
        with open(os.path.join('tariffer', filename), 'r') as f:
            data = yaml.safe_load(f)

        # find current valid tariff
        for t in data['tariffer']:
            if dateutil.parser.parse(t['gyldig_fra']) <= datetime.today() and dateutil.parser.parse(t.get('gyldig_til','2099-01-01')) > datetime.today():
                data['gyldig_tariff'] = t

        if 'gyldig_tariff' not in data:
            print(f'Ingen gyldig tariff for {data["netteier"]}')
            data['gyldig_tariff'] = data['tariffer'][0]

        # Toggles
        data["show_price_signal"] = True

        html = template.render(data)

        output_filename = filename.replace('.yml', '.html')

        with open(os.path.join('docs', 'tariffer', output_filename), 'w') as f:
            f.write(html)

        netteiere.append({
            'netteier': data['netteier'],
            'file': output_filename
        })

# Oversikt

with open('scripts/templates/oversikt.j2.html', 'r') as f:
    template = Template(f.read(),undefined=StrictUndefined)

html = template.render({ 'netteiere' : netteiere })

with open('docs/tariffer/index.html', 'w') as f:
    f.write(html)
