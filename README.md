# ba-api

## Virtual env

Install virtual env

Mac OS\
`python3 -m venv venv`

Windows\
`py -3 -m venv venv`

Activate

Mac OS\
`. venv/bin/activate` or `. venv/bin/activate.fish`

Windows\
`venv\Scripts\activate`

Deactivate\
`deactivate`

Freeze dependencies\
`pip freeze > requirements.txt`

Install dependencies\
`pip install -r requirements.txt`

## Launch

Mac OS\
`export FLASK_APP=setup.py`\
`flask run`

Windows\
`set FLASK_APP=setup.py` or for PowerShell `$env:FLASK_APP='setup.py'`\
`flask run`

To make server publicly available\
`flask run --host=0.0.0.0`

## Debug mode

Activates debugger, automatic reloader\
`export FLASK_ENV=development` or enable debug only:\
`export FLASK_DEBUG=1`

## Configurations

`export FLASK_CONFIG=dev`\
`export FLASK_CONFIG=prod`\
`export FLASK_CONFIG=test`\

## Database

`flask init-db`

## Additional docs

[SQLAlchemy + Flask Tutorial](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/)
[Flask](https://flask.palletsprojects.com/en/1.1.x/)

UUID sample\
`123e4567-e89b-12d3-a456-426655440000`
