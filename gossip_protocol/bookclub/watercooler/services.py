import requests
import redis

import atexit
import random

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


def get_new_favorite():
    """ Returns a new random favorite book for this node. """
    # TODO: implement random book assignment
    return "war and peaces"


def assign_new_favorite():
    """ POST new favorite book to current node. """
    requests.post(
        'http://localhost:' + str(app.config['port']) + '/book',
        data={
            app.config['port']: get_new_favorite()
        })


def favorite_picker_task():
    """ Background task that picks a new favorite book for this node """
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=assign_new_favorite,
        trigger=IntervalTrigger(seconds=random.randint(9, 11)),
        id=app.name + '_favorite_picker',
        name='Pick New Favorite Book',
        replace_existing=True
    )
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())


class RedisWrapper(object):
    def __init__(self, host="localhost", port=6379, db=0):
        self.db = redis.StrictRedis(host=host, port=port, db=db)

    def store(self, node_name, book):
        self.db.set(node_name, book)
