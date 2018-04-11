from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from watercooler.models import Member, Gossip


class MembersView(View):
    def get(self, request):
        members = Member.objects.all()
        return render(request, 'index.html', {'members': members})

    def post(self):
        """
        Update members info and gossip it on!

        Expects post payload like:
        {
            ttl: 3,
            version: 1211,
            port: 5001,
            payload: "Gatsby by Herbert",
            uuid: "asd83jf8j38fj392jf32jf-323f0j0-2903fj2",
        }
        """
        # if this is an old piece of gossip, drop it
        # else update/create action for member and create gossip entry
        #
        # if ttl = 1 don't forward
        # else decrement and forward to all known members except self


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
