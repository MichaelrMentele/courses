from flask import Flask, render_template
from flask import request
import json
import redis


"""
This flask app every ~10 seconds selects a new 'favorite' book from a
list. It then stores this favorite book and multicasts it to all of it's
known peers.
"""
app = Flask(__name__)
app.config['redis_db'] = 0
app.config['port'] = 5000

def new_favorite_book():
    """ Returns a new random favorite book for this node. """
    return "war and peaces"


class RedisWrapper(object):
    def __init__(self, host="localhost", port=6379, db=0):
        self.db = redis.StrictRedis(host=host, port=port, db=db)

    def store(self, node_name, book):
        self.db.set(node_name, book)


@app.route('/peers')
def peers():
    """
    Returns a list of peers.
    """
    pass


@app.route('/book', methods=['GET'])
def book():
    """
    Returns the book associated with this node.
    """
    redis = RedisWrapper(db=app.config['redis_db'])
    book = redis.db.get(app.config['port'])
    if book:
        return book.decode('utf-8')
    else:
        book = new_favorite_book()
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
    """
    # TODO what about TTL?
    # TODO what about forwarding to known nodes?
    redis = RedisWrapper(db=app.config['redis_db'])
    port2book = json.loads(request.get_data().decode('utf-8'))
    for key, val in port2book.items():
        redis.db.set(key, val)


if __name__ == "__main__":
    app.run(port=app.config['port'])
