import string

import factory.fuzzy

from django.contrib.auth.models import User

from api.models import (
    Connection,
    Currency,
    Geolocation,
    Language,
    Location,
    Security,
    TimeZone,
)


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    password = factory.Faker('password')

    class Meta:
        model = User


class FuzzyCode(factory.fuzzy.FuzzyText):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('chars', string.ascii_uppercase)
        super().__init__(*args, **kwargs)


class LanguageFactory(factory.django.DjangoModelFactory):

    code = factory.Faker('language_code')
    name = factory.Faker('language_name')
    native = factory.fuzzy.FuzzyText(length=16)

    class Meta:
        model = Language


class LocationFactory(factory.django.DjangoModelFactory):
    geoname_id = factory.Faker('pyint')
    capital = factory.Faker('city')
    country_flag = factory.Faker('url')
    country_flag_emoji = "🇺🇸"
    country_flag_emoji_unicode = factory.Faker('pystr_format', string_format="U+####")
    calling_code = factory.Faker('pyint', min_value=10, max_value=99)
    is_eu = factory.Faker('pybool')

    @factory.post_generation
    def languages(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for lang in extracted:
                self.languages.add(lang)

    class Meta:
        model = Location


class CurrencyFactory(factory.django.DjangoModelFactory):
    code = factory.Faker('currency_code')
    name = factory.Faker('currency_name')
    plural = factory.LazyAttribute(lambda o: o.name + 's')
    symbol = factory.Faker('currency_symbol')
    symbol_native = factory.LazyAttribute(lambda o: o.symbol)

    class Meta:
        model = Currency


class ConnectionFactory(factory.django.DjangoModelFactory):
    asn = factory.Faker('pyint')
    isp = factory.Faker('company')

    class Meta:
        model = Connection


class SecurityFactory(factory.django.DjangoModelFactory):
    is_proxy = factory.Faker('pybool')
    proxy_type = 'web'
    is_crawler = factory.Faker('pybool')
    crawler_name = None
    crawler_type = None
    is_tor =factory.Faker('pybool')
    threat_level = "low"
    threat_types = None

    class Meta:
        model = Security


class TimeZoneFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('timezone')
    current_time = factory.Faker('date_time')
    gmt_offset = factory.Faker('pyint')
    code = factory.LazyAttribute(lambda o: o.id[:3].upper())
    is_daylight_saving = factory.Faker('pybool')

    class Meta:
        model = TimeZone


class GeolocationFactory(factory.django.DjangoModelFactory):
    # for excercise purposes I'm creating only ipv4 type ip

    ip = factory.Faker('ipv4')
    type = 'ipv4'
    continent_code = FuzzyCode(length=2)
    continent_name = factory.fuzzy.FuzzyText(length=16)
    country_code = factory.Faker('country_code')
    country_name = factory.Faker('country')
    region_code = FuzzyCode(length=2)
    region_name = factory.fuzzy.FuzzyText(length=16)
    city = factory.Faker('city')
    zip = factory.Faker('postcode')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    location = factory.SubFactory(LocationFactory)
    currency = factory.SubFactory(CurrencyFactory)
    connection = factory.SubFactory(ConnectionFactory)
    security = factory.SubFactory(SecurityFactory)
    timezone = factory.SubFactory(TimeZoneFactory)

    class Meta:
        model = Geolocation

