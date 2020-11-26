import pytest
import factory

from rest_framework.test import APIClient

from api.tests.factories import (
    ConnectionFactory,
    CurrencyFactory,
    GeolocationFactory,
    LanguageFactory,
    LocationFactory,
    SecurityFactory,
    TimeZoneFactory,
    UserFactory,
)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def default_geolocation():
    return GeolocationFactory()


@pytest.fixture
def default_user():
    return UserFactory()


@pytest.fixture
def geolocation_dict():
    geolocation_dict = factory.build(dict, FACTORY_CLASS=GeolocationFactory)
    location = factory.build(dict, FACTORY_CLASS=LocationFactory)
    l = factory.build(dict, FACTORY_CLASS=LanguageFactory)
    location["languages"] = [l]
    geolocation_dict["location"] = location
    geolocation_dict["security"] = factory.build(dict, FACTORY_CLASS=SecurityFactory)
    geolocation_dict["connection"] = factory.build(dict, FACTORY_CLASS=ConnectionFactory)
    geolocation_dict["currency"] = factory.build(dict, FACTORY_CLASS=CurrencyFactory)
    geolocation_dict.pop("timezone")
    return geolocation_dict

