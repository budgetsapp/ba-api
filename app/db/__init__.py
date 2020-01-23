
import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app):
    db.init_app(app)

    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    # import is important
    import app.db.models
    # then create
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')
