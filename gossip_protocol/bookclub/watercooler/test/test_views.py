from django.test import TestCase
from django.test import Client

from watercooler.models import Member, Gossip
from sauron.tests.factories import MemberFactory, GossipFactory


class MemberViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_without_members(self):
        response = self.client.get('/watercooler/members')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(
            response,
            'Noone at the watercooler...'
        )

    def test_index_with_members(self):
        for _ in range(0, 10):
            MemberFactory()

        response = self.client.get('/watercooler/members/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, '<ul>')


class GossipViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_with_no_gossip(self):
        response = self.client.get('/watercooler/members')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(
            response,
            'Silence at the watercooler...'
        )

    def test_index_with_gossip(self):
        for _ in range(0, 10):
            GossipFactory()

        response = self.client.get('/watercooler/members/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, '<ul>')

    def test_updating_gossip(self):
        self.client.post('/watercooler/gossip/', {})
        john = MemberFactory()

        response = self.client.post(
            '/watercooler/members/' + john.id,
            {'port': john.port, 'book': 'Moby Dick'}
        )
        john.refresh_from_db()

        self.assertEqual(john.favorite_book, 'Moby Dick')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Gossip.objects.all().count(), 1)
        self.assertEqual(Member.objects.all().count(), 1)
        raise("Not implemented: pass gossip on!")


    def test_new_member_gossip(self):
        self.client.post('/watercooler/gossip/', {})

        response = self.client.post(
            '/watercooler/members/' + 5001, # TODO is this right?
            {'port': 5001, 'book': 'Moby Dick'}
        )

        john = Member.objects.get(port=5001)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(john.favorite_book, 'Moby Dick')
        self.assertEqual(Gossip.objects.all().count(), 1)
        self.assertEqual(Member.objects.all().count(), 1)
        raise("Not implemented: pass gossip on!")
