# django_restAPI_template

Template for restAPI in Django Python

## Set Python environment

```
For Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

For Windows
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

.\.venv\Scripts\activate
```

## Check current Python path

```
where python
```

## Install packages

```
pip install -r requirements.txt
```

## Run Application

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Mac odbc driver

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18 mssql-tools18
```

## Window odbc driver

```
msiexec /i msodbcsql.msi ADDLOCAL=ALL
```

## Deployment

```
In settings.py set Debug = False
Then run command
python manage.py collectstatic
```
