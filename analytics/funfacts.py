#!/usr/bin/env python3
"""
Generate fun facts from the fri-nettleie tariff data.
"""

import os
import yaml
import statistics
import json
from datetime import datetime, date
import dateutil.parser

def is_tariff_valid_now(tariff):
    """Check if a tariff is valid today."""
    today = date.today()
    
    gyldig_fra_str = tariff.get('gyldig_fra')
    if gyldig_fra_str:
        try:
            gyldig_fra = dateutil.parser.parse(gyldig_fra_str).date()
            if today < gyldig_fra:
                return False
        except:
            return False
    
    gyldig_til_str = tariff.get('gyldig_til')
    if gyldig_til_str:
        try:
            gyldig_til = dateutil.parser.parse(gyldig_til_str).date()
            if today >= gyldig_til:
                return False
        except:
            pass
    
    return True

def load_tariff_data():
    """Load all tariff YAML files."""
    tariffs = {}
    tariffer_path = os.path.join(os.path.dirname(__file__), '..', 'tariffer')
    
    for filename in os.listdir(tariffer_path):
        if filename.endswith('.yml'):
            with open(os.path.join(tariffer_path, filename), 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                tariffs[filename[:-4]] = data
    
    return tariffs

def analyze_energy_prices(tariffs):
    """Find highest/lowest energy prices for currently valid tariffs."""
    energy_prices = []
    
    for name, data in tariffs.items():
        netteier = data.get('netteier', name)
        for tariff in data.get('tariffer', []):
            if is_tariff_valid_now(tariff) and 'energiledd' in tariff and 'grunnpris' in tariff['energiledd']:
                price = tariff['energiledd']['grunnpris']
                energy_prices.append((netteier, price, name))
    
    energy_prices.sort(key=lambda x: x[1])
    
    return {
        'lowest': energy_prices[0] if energy_prices else None,
        'highest': energy_prices[-1] if energy_prices else None,
        'average': statistics.mean([p[1] for p in energy_prices]) if energy_prices else 0,
        'median': statistics.median([p[1] for p in energy_prices]) if energy_prices else 0
    }


def analyze_fixed_charges(tariffs):
    """Find highest fixed charges (0 kW tier) for currently valid tariffs."""
    fixed_charges = []
    
    for name, data in tariffs.items():
        netteier = data.get('netteier', name)
        for tariff in data.get('tariffer', []):
            if is_tariff_valid_now(tariff) and 'fastledd' in tariff and 'terskler' in tariff['fastledd']:
                terskler = tariff['fastledd']['terskler']
                # Find the 0 kW tier or first tier
                zero_tier = next((t for t in terskler if t.get('terskel', 0) == 0), terskler[0])
                price = zero_tier['pris']
                fixed_charges.append((netteier, price, name))
    
    fixed_charges.sort(key=lambda x: x[1], reverse=True)
    return fixed_charges

def analyze_tariff_complexity(tariffs):
    """Analyze tariff complexity - find companies with most power tiers (terskler) in current tariffs."""
    complexity = []
    
    for name, data in tariffs.items():
        netteier = data.get('netteier', name)
        max_terskler = 0
        
        for tariff in data.get('tariffer', []):
            if is_tariff_valid_now(tariff) and 'fastledd' in tariff and 'terskler' in tariff['fastledd']:
                terskler_count = len(tariff['fastledd']['terskler'])
                max_terskler = max(max_terskler, terskler_count)
        
        complexity.append((netteier, max_terskler, name))
    
    complexity.sort(key=lambda x: x[1], reverse=True)
    return complexity

def analyze_update_frequency(tariffs):
    """Analyze how often tariffs are updated."""
    updates = []
    today = datetime.now().date()
    
    for name, data in tariffs.items():
        netteier = data.get('netteier', name)
        sist_oppdatert = data.get('sist_oppdatert')
        
        if sist_oppdatert:
            try:
                update_date = dateutil.parser.parse(sist_oppdatert).date()
                days_since_update = (today - update_date).days
                
                # Only include updates that are not in the future as there shouldn't be
                # should track the ones that are somewhere else
                if days_since_update >= 0:
                    updates.append((netteier, update_date, days_since_update, name))
            except:
                pass
    
    updates.sort(key=lambda x: x[2])
    return updates

def analyze_geographical_spread(tariffs):
    """Analyze geographical and size diversity."""
    total_companies = len(tariffs)
    
    multi_gln = 0
    max_glns = 0
    max_gln_company = ""
    
    for name, data in tariffs.items():
        glns = data.get('gln', [])
        if isinstance(glns, list) and len(glns) > 1:
            multi_gln += 1
            if len(glns) > max_glns:
                max_glns = len(glns)
                max_gln_company = data.get('netteier', name)
    
    return {
        'total': total_companies,
        'multi_gln': multi_gln,
        'max_glns': max_glns,
        'max_gln_company': max_gln_company
    }

def generate_funfacts_summary():
    """Generate a brief summary of fun facts for console output."""
    
    funfacts = generate_funfacts_json()
    
    print("FRI-NETTLEIE SUMMARY")
    print("=" * 30)
    print(f"Total companies: {funfacts['meta']['total_companies']}")
    
    energy = funfacts['energy_prices']
    print(f"Energy price range: {energy['cheapest']['price_ore_kwh']} - {energy['most_expensive']['price_ore_kwh']} øre/kWh")
    
    fixed = funfacts['fixed_charges']
    print(f"Fixed charge range: {fixed['lowest']['amount_kr_year']:_} - {fixed['highest']['amount_kr_year']:_} kr/year".replace('_', ' '))
    
    print(f"Companies with multiple power tiers: {funfacts['complexity']['companies_with_multiple_tiers']}")
    print("JSON output generated successfully!")

def generate_funfacts_json():
    """Generate fun facts as structured JSON data."""
    
    tariffs = load_tariff_data()
    
    energy = analyze_energy_prices(tariffs)
    fixed = analyze_fixed_charges(tariffs)
    complexity = analyze_tariff_complexity(tariffs)
    updates = analyze_update_frequency(tariffs)
    geo = analyze_geographical_spread(tariffs)
    
    funfacts = {
        "meta": {
            "generated_at": datetime.now().isoformat(),
            "total_companies": geo['total']
        },
        "energy_prices": {
            "cheapest": {
                "company": energy['lowest'][0] if energy['lowest'] else None,
                "price_ore_kwh": energy['lowest'][1] if energy['lowest'] else None
            },
            "most_expensive": {
                "company": energy['highest'][0] if energy['highest'] else None,
                "price_ore_kwh": energy['highest'][1] if energy['highest'] else None
            },
            "price_spread_ore_kwh": energy['highest'][1] - energy['lowest'][1] if energy['lowest'] and energy['highest'] else None,
            "average_ore_kwh": round(energy['average'], 1),
            "median_ore_kwh": round(energy['median'], 1)
        },
        "fixed_charges": {
            "highest": {
                "company": fixed[0][0] if fixed else None,
                "amount_kr_year": fixed[0][1] if fixed else None
            },
            "lowest": {
                "company": min(fixed, key=lambda x: x[1])[0] if fixed else None,
                "amount_kr_year": min(fixed, key=lambda x: x[1])[1] if fixed else None
            },
            "average_kr_year": round(statistics.mean([f[1] for f in fixed]), 0) if fixed else None,
            "spread_kr_year": fixed[0][1] - min(fixed, key=lambda x: x[1])[1] if fixed else None
        },
        "complexity": {
            "most_complex": {
                "company": complexity[0][0] if complexity else None,
                "power_tiers": complexity[0][1] if complexity else None
            },
            "companies_with_multiple_tiers": len([c for c in complexity if c[1] > 1]) if complexity else 0
        },
        "updates": {
            "most_recent": {
                "company": updates[0][0] if updates else None,
                "days_ago": updates[0][2] if updates else None,
                "date": updates[0][1].isoformat() if updates else None
            },
            "oldest": {
                "company": updates[-1][0] if updates else None,
                "days_ago": updates[-1][2] if updates else None,
                "date": updates[-1][1].isoformat() if updates else None
            },
            "updated_last_30_days": len([u for u in updates if u[2] <= 30]) if updates else 0
        },
        "coverage": {
            "large_companies_multiple_areas": geo['multi_gln'],
            "largest_coverage": {
                "company": geo['max_gln_company'] if geo['max_gln_company'] else None,
                "area_count": geo['max_glns']
            }
        }
    }
    
    return funfacts

def save_funfacts_json(filename="funfacts.json"):
    """Save fun facts to JSON file."""
    funfacts = generate_funfacts_json()
    
    output_path = os.path.join(os.path.dirname(__file__), filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(funfacts, f, indent=2, ensure_ascii=False)
    
    print(f"Fun facts saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    save_funfacts_json()
    print()
    generate_funfacts_summary()