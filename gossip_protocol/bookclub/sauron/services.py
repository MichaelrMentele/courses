from functools import wraps


class AllSeeingEye(object):
    def __init__(self, config={}):
        self.config = config

    def see(response):
        print('Reporting to Sauron!')
        raise("Not Implemented")

    def all_seeing_eye(self, func):
        """
        Publishes to Sauron log aggregator.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            self.see(response)
            return response
        return wrapper
