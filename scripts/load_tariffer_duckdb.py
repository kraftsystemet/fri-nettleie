import os
import glob
import yaml
import pandas as pd
import duckdb
import tempfile
from datetime import datetime


def parse_date(val):
    if not val:
        return None
    try:
        return datetime.strptime(str(val), "%Y-%m-%d").date()
    except Exception:
        return None


# List all top-level *.yml files in /tariffer (repo root, not script/)
REPO_ROOT = os.path.dirname(os.path.dirname(__file__))
TARIFF_PATH = os.path.join(REPO_ROOT, "tariffer")
files = [
    f
    for f in glob.glob(os.path.join(TARIFF_PATH, "*.yml"))
    if os.path.isfile(f) and "/old/" not in f
]


def to_array(val):
    if val is None:
        return []
    if isinstance(val, list):
        return val
    return [val]


def extract_tables(filenames):
    from datetime import date

    today = date.today()
    (
        netteier_rows,
        tariff_rows,
        energiledd_rows,
        fastledd_rows,
        terskel_rows,
        unntak_rows,
    ) = [], [], [], [], [], []
    netteier_id_ctr = tariff_id_ctr = energiledd_id_ctr = fastledd_id_ctr = (
        terskel_id_ctr
    ) = unntak_id_ctr = 1
    for filename in filenames:
        with open(filename, encoding="utf-8") as f:
            doc = yaml.safe_load(f)
        # Filter current tariffs
        current_tariffs = []
        for tariff in doc.get("tariffer", []):
            fra = parse_date(tariff.get("gyldig_fra"))
            til = parse_date(tariff.get("gyldig_til"))
            if not fra or fra > today:
                continue  # Skip invalid or future not started
            if til and til <= today:
                continue  # Expired tariff
            current_tariffs.append(tariff)
        if not current_tariffs:
            continue  # Exclude nettierer with no current tariffs
        netteier_id = netteier_id_ctr
        netteier_id_ctr += 1
        netteier_row = {
            "id": netteier_id,
            "netteier": doc.get("netteier"),
            "sist_oppdatert": parse_date(doc.get("sist_oppdatert")),
            "gln": to_array(doc.get("gln")),
            "mga": to_array(doc.get("mga")),
            "kilder": to_array(doc.get("kilder")),
        }
        netteier_rows.append(netteier_row)
        for tariff in current_tariffs:
            tariff_id = tariff_id_ctr
            tariff_id_ctr += 1
            tariff_row = {
                "id": tariff_id,
                "netteier_id": netteier_id,
                "navn": tariff.get("navn"),
                "gyldig_fra": parse_date(tariff.get("gyldig_fra")),
                "gyldig_til": parse_date(tariff.get("gyldig_til")),
                "kundegrupper": to_array(tariff.get("kundegrupper")),
            }
            tariff_rows.append(tariff_row)
            energiledd = tariff.get("energiledd", {})
            energiledd_id = energiledd_id_ctr
            energiledd_id_ctr += 1
            energiledd_row = {
                "id": energiledd_id,
                "tariff_id": tariff_id,
                "grunnpris": energiledd.get("grunnpris"),
            }
            energiledd_rows.append(energiledd_row)
            for unntak in energiledd.get("unntak", []) or []:
                unntak_id = unntak_id_ctr
                unntak_id_ctr += 1
                unntak_row = {
                    "id": unntak_id,
                    "energiledd_id": energiledd_id,
                    "navn": unntak.get("navn"),
                    "timer": unntak.get("timer"),
                    "dager": to_array(unntak.get("dager")),
                    "måneder": to_array(unntak.get("måneder")),
                    "pris": unntak.get("pris"),
                }
                unntak_rows.append(unntak_row)
            fastledd = tariff.get("fastledd", {})
            fastledd_id = fastledd_id_ctr
            fastledd_id_ctr += 1
            fastledd_row = {
                "id": fastledd_id,
                "tariff_id": tariff_id,
                "metode": fastledd.get("metode"),
                "terskel_inkludert": fastledd.get("terskel_inkludert"),
            }
            fastledd_rows.append(fastledd_row)
            for terskel in fastledd.get("terskler", []) or []:
                terskel_id = terskel_id_ctr
                terskel_id_ctr += 1
                terskel_row = {
                    "id": terskel_id,
                    "fastledd_id": fastledd_id,
                    "terskel": terskel.get("terskel"),
                    "pris": terskel.get("pris"),
                }
                terskel_rows.append(terskel_row)
    return (
        netteier_rows,
        tariff_rows,
        energiledd_rows,
        fastledd_rows,
        terskel_rows,
        unntak_rows,
    )


def df_array_cast(df, array_cols):
    for col in array_cols:
        if col in df:
            df[col] = df[col].apply(
                lambda v: v if isinstance(v, list) else ([] if v is None else [v])
            )
    return df


def main():
    (
        netteier_rows,
        tariff_rows,
        energiledd_rows,
        fastledd_rows,
        terskel_rows,
        unntak_rows,
    ) = extract_tables(files)

    # DataFrame creation
    df_netteier = pd.DataFrame(netteier_rows)
    df_tariff = pd.DataFrame(tariff_rows)
    df_energiledd = pd.DataFrame(energiledd_rows)
    df_fastledd = pd.DataFrame(fastledd_rows)
    df_terskel = pd.DataFrame(terskel_rows)
    df_unntak = pd.DataFrame(unntak_rows)
    # Ensure arrays
    df_netteier = df_array_cast(df_netteier, ["gln", "mga", "kilder"])
    df_tariff = df_array_cast(df_tariff, ["kundegrupper"])
    df_unntak = df_array_cast(df_unntak, ["dager", "måneder"])
    # Generate a unique dot-prefixed db path in cwd WITHOUT precreating the file
    import uuid

    db_path = os.path.join(REPO_ROOT, f".normalized_tariffs_{uuid.uuid4().hex}.db")

    con = duckdb.connect(db_path)
    # Define DDL (array fields explicitly as ARRAY(TEXT))
    con.execute("""
        CREATE TABLE netteier (
            id INTEGER PRIMARY KEY,
            netteier TEXT,
            sist_oppdatert DATE,
            gln TEXT[],
            mga TEXT[],
            kilder TEXT[]
        );
        CREATE TABLE tariff (
            id INTEGER PRIMARY KEY,
            netteier_id INTEGER REFERENCES netteier(id),
            navn TEXT,
            gyldig_fra DATE,
            gyldig_til DATE,
            kundegrupper TEXT[]
        );
        CREATE TABLE energiledd (
            id INTEGER PRIMARY KEY,
            tariff_id INTEGER REFERENCES tariff(id),
            grunnpris DOUBLE
        );
        CREATE TABLE fastledd (
            id INTEGER PRIMARY KEY,
            tariff_id INTEGER REFERENCES tariff(id),
            metode TEXT,
            terskel_inkludert BOOLEAN
        );
        CREATE TABLE terskel (
            id INTEGER PRIMARY KEY,
            fastledd_id INTEGER REFERENCES fastledd(id),
            terskel INTEGER,
            pris DOUBLE
        );
        CREATE TABLE unntak (
            id INTEGER PRIMARY KEY,
            energiledd_id INTEGER REFERENCES energiledd(id),
            navn TEXT,
            timer TEXT,
            dager TEXT[],
            måneder TEXT[],
            pris DOUBLE
        );
    """)
    # DataFrame loading to DuckDB in warning-free way
    # Use duckdb's own DataFrame registration and simple INSERTs
    tables = [
        ("netteier", df_netteier),
        ("tariff", df_tariff),
        ("energiledd", df_energiledd),
        ("fastledd", df_fastledd),
        ("terskel", df_terskel),
        ("unntak", df_unntak),
    ]
    for name, df in tables:
        con.register("df_tmp", df)
        # Insert all rows
        if len(df.columns) > 0 and len(df) > 0:
            colstr = ",".join(df.columns)
            con.execute(f"INSERT INTO {name} ({colstr}) SELECT {colstr} FROM df_tmp;")
        con.unregister("df_tmp")

    con.close()

    print(
        f"Tariffer normalisert og lastet inn i DuckDB: {db_path}\nStarter DuckDB shell ... (trykk Ctrl-D for å avslutte)"
    )
    os.system(f"duckdb {db_path}")
    # Optionally: delete temp file
    try:
        os.remove(db_path)
    except Exception:
        pass


if __name__ == "__main__":
    main()
