import json
import uuid

import redis
import requests
from flask.views import View
from flask import request

from helpers.helpers import get_new_favorite
from flask.views import MethodView


class MemberAPI(MethodView):
    def __init__(self, port, redis):
        self.redis = redis
        self.port = port

    def get(self, member_port):
        """
        Returns a list of peers to books.
        """
        if member_port:
            book = self.redis.db.get(self.port)
            if book:
                return book.decode('utf-8')
            else:
                book = get_new_favorite()
                self.redis.store(self.port, book)
                return book
        # return all books
        else:
            node2books = {}

            for key in self.redis.db.keys():
                node2books[key.decode('utf-8')] = self.redis.db.get(key).decode('utf-8')
            return (
                json.dumps({'success': True, node2books: node2books}),
                200, {'ContentType': 'application/json'}
            )

    def post(self):
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
        port2book = json.loads(request.get_data().decode('utf-8'))
        for key, val in port2book.items():
            self.redis.db.set(key, val)


class UpdateFavoriteView(View):
    def __init__(self, port, redis):
        self.port = port
        self.redis = redis

    def dispatch_request(self):
        book = request.get_data().decode('utf-8')
        self._create_book(book)
        self._gossip(book)

        return (
            json.dumps({'success': True}),
            200, {'ContentType': 'application/json'}
        )

    def _create_book(self, book):
        self.redis.db.set(self.port, book)

    def _gossip(self, book):
        node_ports = [port.decode('utf-8') for port in redis.db.keys()]
        for port in node_ports:
            # Don't gossip with yourself!
            if not port == self.property:
                print('Forwarding to: ' + port)
                requests.post(
                    'http://localhost:' + port + '/gossip',
                    data={
                        'uuid': str(uuid.uuid4()),
                        'ttl': 3,
                        'payload': book,
                        'sender_port': self.port,
                    })
