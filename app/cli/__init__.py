
import click
from flask.cli import with_appcontext
from app.extensions import db


def init_cli_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(load_db_data_command)


def init_db():
    # import is important
    import app.models
    # then create
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def get_item_by_value(items, key, value):  # TODO: move to utils/helpers
    match = None
    for item in items:
        if item[key] == value:
            match = item
            break
    return match


def add_category(categories_seed_data, display_name, user_id):
    from app.models import Category
    from app.helpers.datetime import dt_from_str
    category_raw = get_item_by_value(
        categories_seed_data, "display_name", display_name)
    category = Category(id=category_raw["id"],
                        display_name=category_raw["display_name"],
                        created_at=dt_from_str(category_raw["created_at"]),
                        user_id=user_id)
    db.session.add(category)


def load_db_data():
    import json
    import os

    root = os.path.realpath(os.path.dirname(__file__))

    # users data
    users_seed_data = json.load(open(os.path.join(root, "users.json")))
    ba_user_1_raw = get_item_by_value(users_seed_data, "login", "ba-user-1")

    # categories data
    categories_seed_data = json.load(
        open(os.path.join(root, "categories.json")))

    add_category(categories_seed_data, 'taxi', ba_user_1_raw['id'])
    add_category(categories_seed_data, 'fastfood', ba_user_1_raw['id'])

    # expenses data

    # commit
    db.session.commit()


@click.command("load-db-data")
@with_appcontext
def load_db_data_command():
    load_db_data()
    click.echo('Loaded data')
