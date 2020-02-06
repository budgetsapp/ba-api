# ba-api

## Configurations

`export FLASK_CONFIG=dev`\
`export FLASK_CONFIG=prod`\
`export FLASK_CONFIG=test`\

## Database

`flask init-db` - creates local database\
`flask load-db-data` - fill database with seed data

## Additional docs

[SQLAlchemy + Flask Tutorial](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/)
[Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Notes

Variables set on the command line are used over those set in `.env`, which are used over those set in `.flaskenv`.
`.flaskenv` should be used for public variables, such as `FLASK_APP`, while `.env` should not be committed to your repository so that it can set private variables.

The files are only loaded by the flask command or calling `run()`. If you would like to load these files when running in production, you should call `load_dotenv()` manually
