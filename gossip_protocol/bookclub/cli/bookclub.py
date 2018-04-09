import click
import redis
from member import RedisWrapper


@click.command()
def new():
    """ Adds a new member to the bookclub """
    # fetch a random seed member
    # create a new member
    pass


@click.command()
def members():
    """ Fetches a list of all the members of the bookclub """
    # fetch all members of the book club
    # print to the command line
    pass


@click.command()
def clean():
    """ Destroys all saved state and cleans up member processes """
    redis = RedisWrapper()
    redis.db.flushall()
    # TODO: kill processes
