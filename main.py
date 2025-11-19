import os
from pathlib import Path
import pyodbc
import pandas as pd


TABLES = [
    "parent_demographics_2025",
    "child_demographics_2025",
    "qualtrics_parent_data_2025",
    "qualtrics_children_data_2025",
    "asa24_parents_totals_2025",
    "asa24_parents_items_2025",
    "asa24_children_totals_2025",
    "asa24_children_items_2025",
    "children_self_report_2025",
    "ethnicity_children_2025",
    "ethnicity_children_mixed_details_2025",
    "ethnicity_parents_2025",
    "ethnicity_parents_mixed_details_2025",
    "families_2025",
    "life_labs_2025",
    "parents_2025",
    "participants_2025",
    "qualtrics_parent_data_coded_2025",
    "qualtrics_children_data_coded_2025",
]


def fetch_table(table_name, conn):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    return df


def export_table(table_name, conn, out_dir: Path):
    df = fetch_table(table_name, conn)
    out_path = out_dir / f"{table_name}.csv"
    df.to_csv(out_path, index=False)
    print(f"Data exported to {out_path}")


def load_env_file(dotenv_path: Path) -> None:
    """
    Minimal .env loader to avoid extra dependencies.
    Loads KEY=VALUE lines into os.environ if not already set.
    """
    if not dotenv_path.exists():
        return
    try:
        with dotenv_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip("'").strip('"')
                if key and key not in os.environ:
                    os.environ[key] = value
    except Exception:
        # Silent fallback; script will later validate required vars
        pass


def main():
    # Load .env from the script directory if present
    script_dir = Path(__file__).resolve().parent
    load_env_file(script_dir / ".env")
    output_dir = script_dir / "outputs"
    output_dir.mkdir(exist_ok=True)

    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    driver = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

    missing = [name for name, val in [
        ("DB_SERVER", server),
        ("DB_DATABASE", database),
        ("DB_USERNAME", username),
        ("DB_PASSWORD", password),
    ] if not val]
    if missing:
        print("Missing required DB settings: " + ", ".join(missing))
        print("Provide them via environment variables or a .env file next to main.py.")
        print("Expected keys: DB_SERVER, DB_DATABASE, DB_USERNAME, DB_PASSWORD, optional DB_DRIVER.")
        return

    conn = pyodbc.connect(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )

    try:
        print('Enter "all" to pull all tables, or enter a single table name (see README for list).')
        user_input = input("Table name or 'all': ").strip()
        if not user_input:
            print("No input provided. Exiting.")
            return

        if user_input.lower() == "all":
            for table in TABLES:
                export_table(table, conn, output_dir)
            print("Export completed.")
        else:
            table = user_input
            if table not in TABLES:
                print("Table not recognized. See README for the list of supported tables.")
                return
            export_table(table, conn, output_dir)
            print("Export completed.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()


