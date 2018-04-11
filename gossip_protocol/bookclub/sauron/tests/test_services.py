from django.test import TestCase
from sauron.services import AllSeeingEye


class AllSeeingEyeTest(TestCase):

    def test_all_seeing_eye_can_see(self):
        # wrap something with all seeing eye
        # verify it tries to send a request
        # verify function returned is one wrapped
        raise('not implemented')

    def test_seeing(self):
        # pass something to see
        # verify it tries to send a request -- maybe use vcr?
        raise('not implemented')
