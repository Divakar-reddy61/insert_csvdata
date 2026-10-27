# ProjectCSV

A Django project for storing bank and bank branch information from CSV files.
The `Bank` and `Branch` models are available in the Django admin.

## Requirements

- Python 3.10 or later
- Django 5.2.16

## Setup

Run these commands from the project directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install Django==5.2.16
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/` for the Django admin. Create an
administrator account first with:

```powershell
python manage.py createsuperuser
```

The project uses SQLite by default and creates `db.sqlite3` in the project
directory.

## Data endpoints

- `/insert_data/` imports bank names from `app/bank.csv`.
- `/insert_branch_data/` imports branch rows from `app/branch1.csv`, linking
  each row to a bank with a matching name.
- `/delete_branch_data/` deletes **all** branch records.

These endpoints currently use hard-coded Windows file paths in
`app/views.py`. Update those paths to match your local project location before
using the import endpoints. The delete endpoint is destructive and should only
be used when you intend to remove every branch record.

## CSV files

- `app/bank.csv` contains bank names.
- `app/branch1.csv` contains a header row followed by bank and branch details:
  bank, IFSC, branch, address, contact, city, district, and state.

## Development

Apply model changes with:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Run the test suite with:

```powershell
python manage.py test
```

The settings currently contain a development secret key and have `DEBUG`
enabled. Do not use the default settings as-is in production.
