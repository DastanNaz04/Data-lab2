# src/loader.py

import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

CLEAN_CSV = os.path.join(DATA_DIR, "clean.csv")
DB_PATH = os.path.join(DATA_DIR, "marketcap.db")


def load_to_sqlite():
    print("[LOADER] Loading clean.csv...")

    df = pd.read_csv(CLEAN_CSV)
    print(f"[LOADER] Loaded {df.shape[0]} rows")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # создаём таблицу
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto (
            rank INTEGER,
            name TEXT,
            symbol TEXT,
            price REAL,
            market_cap REAL,
            volume_24h REAL,
            circulating_supply REAL,
            percent_change_1h REAL,
            percent_change_24h REAL,
            percent_change_7d REAL
        );
    """)

    # очистка таблицы перед новой загрузкой
    cursor.execute("DELETE FROM crypto;")

    # вставляем строки
    df.to_sql("crypto", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()

    print(f"[LOADER] Inserted {df.shape[0]} rows into marketcap.db (table: crypto)")
    print(f"[LOADER] Database saved at: {DB_PATH}")


def run():
    load_to_sqlite()


if __name__ == "__main__":
    run()
