# project/commands.py
import click
from flask.cli import with_appcontext
from project.seed import seed_data

@click.command(name='seed_db')
@with_appcontext
def seed_db():
    seed_data()
