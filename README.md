## DB-pull Setup & Usage Guide

👉Quick install instructions to run either scripts.

### macOS

1) Install Python
- Download from `https://www.python.org/downloads/` and install (recommended), or:
- With Homebrew:
```bash
brew install python
```

2) Create a virtual environment (optional but recommended) and install packages
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pandas pyodbc
```

### Windows

1) Install Python
- Download from `https://www.python.org/downloads/windows/` and run the installer.
- Check “Add python.exe to PATH” during install.

2) Create a virtual environment (optional but recommended) and install packages
```bash
python -m venv .venv
.\\.venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install pandas pyodbc
```

### Create a .env file
In the `DB-pull` folder, create a file named `.env` with the following contents. Replace `replace_me` with your actual password.

```bash
DB_SERVER=msdatatest2022.cfs.uoguelph.ca
DB_DATABASE=GFHS_PSDB
DB_USERNAME=gfhsUser
DB_PASSWORD=replace_me
DB_DRIVER=ODBC Driver 17 for SQL Server
```

## Running Script
1) Activate the virtual environment

macOS
```bash
source .venv/bin/activate
```
Windows
```bash
.\.venv\Scripts\activate
```

2) Run the script
```bash
python main.py
```

### 📊Tables you can pull

- parent_demographics_2025
- child_demographics_2025
- qualtrics_parent_data_2025
- qualtrics_children_data_2025
- asa24_parents_totals_2025
- asa24_parents_items_2025
- asa24_children_totals_2025
- asa24_children_items_2025
- children_self_report_2025
- ethnicity_children_2025
- ethnicity_children_mixed_details_2025
- ethnicity_parents_2025
- ethnicity_parents_mixed_details_2025
- families_2025
- life_labs_2025
- parents_2025
- participants_2025
- qualtrics_parent_data_coded_2025
- qualtrics_children_data_coded_2025
