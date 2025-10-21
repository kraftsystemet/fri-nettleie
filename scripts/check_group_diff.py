#!/usr/bin/env python3
"""
Check for differences between corresponding files in naring and privat tariff folders.
Output is list of files where tariffs differ meaningfully.

What is considered "meaningful" difference:
- Energiledd in privat tariffs is exactly 1 øre higher than in naring tariffs
- Fastledd in privat tariffs is exactly 800 kr higher than in corresponding naring tariffs

Has two runmodes:
- Default: 
    just shows summary of files where privat and naring tariffs differ meaningfully.

- Detailed (--detailed or -d):
    Shows one diff at a time, waits for Enter to continue or 'q' to quit and see summary.
    Summary is only shown for tariffs that has been looked at in detail before quitting.

Usage:
    python3 scripts/check_group_diff.py [--detailed]
"""

import os
import subprocess
import yaml
import math
import sys

NARING_DIR = './referanse-data/nve/tariffer/naring'
PRIVAT_DIR = './referanse-data/nve/tariffer/privat'

def load_tariff_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
    
def advanced_compare_energiledd(naring_data, privat_data):
    """
    Comparing the energiledd sections of naring and privat tariffs.
    Privat has +1 øre in energiledd in enova tax compared to naring
    """
    equal = all((pd - nd) == 1 for nd, pd in zip(naring_data["energiledd"], privat_data["energiledd"]))
    return equal

def advanced_compare_fastledd(naring_data, privat_data):
    """
    Comparing the fastledd sections of naring and privat tariffs.
    Privat has +800 øre in fastledd in enova tax compared to naring
    """
    privat_dict = { item["terskel"]: item["pris"] for item in privat_data["terskler"] }

    equal = all(
        math.isclose(
            item["pris"] - privat_dict.get(item["terskel"], float('inf')),
            800.0,
            rel_tol=0.5 # allowing some tolerance, moms maybe?
        ) for item in naring_data["terskler"] if item["terskel"] in privat_dict
    )
    return equal

def check_group_diff(detailed: bool = False):
    naring_files = [f for f in os.listdir(NARING_DIR) if f.endswith('.yml')]
    similar_files = []
    for fname in sorted(naring_files)[1:]:
        naring_path = os.path.join(NARING_DIR, fname)
        privat_path = os.path.join(PRIVAT_DIR, fname)
        if not os.path.exists(privat_path):
            print(f"Missing privat file for {fname}")
            continue
        naring_data = load_tariff_data(naring_path)
        privat_data = load_tariff_data(privat_path)

        enova_diff_energiledd = advanced_compare_energiledd(naring_data, privat_data)
        enova_diff_fastledd = advanced_compare_fastledd(naring_data, privat_data)

        if enova_diff_energiledd and enova_diff_fastledd:
            similar_files.append(fname)

        if detailed:
            result = subprocess.run([
                'diff', '--width=100', '--side-by-side', naring_path, privat_path
            ], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"\n=== Diff for {fname} ===")
        
                if enova_diff_energiledd and enova_diff_fastledd:
                    print(
                        "The only differences are in energiledd (+1 øre) and fastledd "
                        "(+800 kr) as expected."
                    )
                    similar_files.append(fname)
                    continue

                if enova_diff_fastledd and not enova_diff_energiledd:
                    print("Fastledd sections differ but _not_ _energiledd_. Check closer.")
                elif not enova_diff_fastledd and enova_diff_energiledd:
                    print("Energiledd sections differ but _not_ _fastledd_. Check closer.")

                print(result.stdout or '[binary or no output]')
                
                inp = input("Press Enter to continue, or type 'q' to quit and see summary: ")
                if inp.strip().lower() == 'q':
                    break

    if similar_files:
        print("\nFiles where privat and naring is the same:")
        for f in similar_files:
            print(f"- {f}")
    else:
        print("\nNo similar files found.")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in ('--detailed', '-d'):
        check_group_diff(detailed=True)
    elif len(sys.argv) > 1:
        print("Usage: check_group_diff.py [--detailed|-d]")
        sys.exit(1)
    else:
        check_group_diff()
