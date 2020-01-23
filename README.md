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
`pip freeze > requirements/shared.txt`

Install dependencies\
`pip install -r requirements/shared.txt`

## Launch

`export FLASK_APP=app.py`
`flask run`

## Additional docs

[SQLAlchemy + Flask Tutorial](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/)
[Flask](https://flask.palletsprojects.com/en/1.1.x/)
