from unittest import TestCase
from sauron.tests.factories.request_factory import RequestFactory
from sauron import sauron


class Sauron(TestCase):
    """ Testcases for the Sauron API """
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_requests_table(self):
        response = self.app.get('/')
        self.assertTrue(
            b'No requests have been seen by the eye.'
            in response.data['message']
        )

    def test_retrieves_all_requests(self):
        for _ in range(0, 10):
            RequestFactory()

        response = self.app.get('/')
        self.assertEqual(len(response.data['requests']), 10)
