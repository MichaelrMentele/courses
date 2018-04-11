from flask.views import MethodView


class SauronAPI(MethodView):
    def get(self):
        """ Fetch aggregated requests """
        # query the DB
        # dump all requests on the client
