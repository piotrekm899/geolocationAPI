import random

from django.core.management.base import BaseCommand

from api.tests.factories import GeolocationFactory, LanguageFactory


class Command(BaseCommand):
    help = 'Fills database with fake data'

    def handle(self, *args, **options):
        geolocs = GeolocationFactory.create_batch(10)
        langs = LanguageFactory.create_batch(15)
        for g in geolocs:
            for r in random.sample(langs, random.randint(1, 2)):
                g.location.languages.add(r)
