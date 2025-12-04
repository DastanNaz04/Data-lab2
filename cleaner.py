# src/cleaner.py

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

RAW_CSV = os.path.join(DATA_DIR, "raw.csv")
CLEAN_CSV = os.path.join(DATA_DIR, "clean.csv")


def clean_value(x):
    if isinstance(x, str):
        x = x.replace("$", "").replace(",", "").replace("%", "").strip()
    try:
        return float(x)
    except:
        return x


def clean_data():
    print("[CLEANER] Loading raw.csv...")

    df = pd.read_csv(RAW_CSV)
    print(f"[CLEANER] Raw shape: {df.shape[0]} rows")

    numeric_cols = [
        "price",
        "market_cap",
        "volume_24h",
        "circulating_supply",
        "percent_change_1h",
        "percent_change_24h",
        "percent_change_7d",
    ]

    for col in numeric_cols:
        df[col] = df[col].apply(clean_value)

    df.to_csv(CLEAN_CSV, index=False)

    print(f"[CLEANER] Cleaned and saved {df.shape[0]} rows → {CLEAN_CSV}")


def run():
    clean_data()


if __name__ == "__main__":
    run()



