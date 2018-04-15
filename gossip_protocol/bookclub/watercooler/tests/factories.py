from faker import Faker
from factory.django import DjangoModelFactory


class MemberFactory(DjangoModelFactory):
    class Meta:
        model = 'watercooler.Member'

    port = Faker().random_int()
    favorite_book = "Moby Dick by Some Guy"
    created_at = Faker().date_time()
    updated_at = Faker().date_time()


class GossipFactory(DjangoModelFactory):
    class Meta:
        model = 'watercooler.Member'

    message = "fake request"
    created_at = Faker().date_time()
