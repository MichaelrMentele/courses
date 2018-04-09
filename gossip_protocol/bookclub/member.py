import json
import sys
import atexit
import random
import uuid

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from flask import Flask, render_template
from flask import request
import redis
import requests


###############
# Handle Args #
###############
try:
    name = sys.argv[1]
except IndexError:
    name = 'roger'

try:
    db = sys.argv[2]
except IndexError:
    db = 0

try:
    port = sys.argv[3]
except IndexError:
    port = 5000

app = Flask(name)
app.config['redis_db'] = int(db)
app.config['port'] = int(port)


###########
# Helpers #
###########
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


##########
# Routes #
##########
@app.route('/peers')
def peers():
    """
    Returns a list of peers.
    """
    pass


@app.route('/book', methods=['POST'])
def create_book():
    # Create new book
    book = request.get_data().decode('utf-8')
    redis = RedisWrapper(db=app.config['redis_db'])
    redis.db.set(app.config['port'], book)

    # Gossip about it
    node_ports = redis.db.keys() # TODO: rethink how my data is stored in redis
    for port in node_ports:
        decoded_port = port.decode('utf-8')
        # Don't gossip to yourself
        # if not int(decoded_port) == app.config['port']:
        print('Forwarding to: ' + decoded_port)
        requests.post(
            'http://localhost:' + decoded_port + '/gossip',
            data={
                'uuid': str(uuid.uuid4()),
                'ttl': 3,
                'payload': book,
                'sender_port': app.config['port']
            })

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/book', methods=['GET'])
def get_book():
    """
    Returns the book associated with this node.
    """
    redis = RedisWrapper(db=app.config['redis_db'])
    book = redis.db.get(app.config['port'])
    if book:
        return book.decode('utf-8')
    else:
        book = get_new_favorite()
        redis.store(app.name, book)
        return book


@app.route('/dashboard', methods=['GET'])
def dashboard():
    """
    Renders an HTML template of a table of the bookclubs favorite books.
    """
    redis = RedisWrapper(db=app.config['redis_db'])
    node2books = {}

    for key in redis.db.keys():
        node2books[key.decode('utf-8')] = redis.db.get(key).decode('utf-8')
    return render_template('dashboard.html', node2books=node2books)


@app.route('/gossip', methods=['POST'])
def gossip():
    """
    Get the passed node name to book and for each node, update it's entry.

    Expects post body like:
    {
        ttl: 3,
        sender_port: 5001,
        payload: "Gatsby by Herbert",
        uuid: "asd83jf8j38fj392jf32jf-323f0j0-2903fj2",
    }
    """
    # TODO what about TTL?
    # TODO what about forwarding to known nodes?
    redis = RedisWrapper(db=app.config['redis_db'])
    port2book = json.loads(request.get_data().decode('utf-8'))
    for key, val in port2book.items():
        redis.db.set(key, val)


if __name__ == "__main__":
    favorite_picker_task()
    app.run(port=app.config['port'])
