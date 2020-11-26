import pytest

from rest_framework import status
from rest_framework.reverse import reverse

from api.models import Geolocation
from api.serializers import GeolocationSerializer


@pytest.mark.django_db
def test_retrieve_not_logged(api_client, default_geolocation):
    url = reverse("geolocation-detail", kwargs={"pk": 1})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_retrieve(api_client, default_geolocation, default_user):
    api_client.force_authenticate(user=default_user)
    url = reverse("geolocation-detail", kwargs={"pk": default_geolocation.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == GeolocationSerializer(default_geolocation).data


@pytest.mark.django_db
def test_destroy(api_client, default_geolocation, default_user):
    api_client.force_authenticate(user=default_user)
    url = reverse("geolocation-detail", kwargs={"pk": default_geolocation.pk})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Geolocation.objects.filter(pk=default_geolocation.pk).exists()


@pytest.mark.django_db
def test_create_without_input(api_client, default_user):
    api_client.force_authenticate(user=default_user)
    url = reverse("geolocation-list")
    response = api_client.post(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["ip_or_url"][0] == "This field is required."


@pytest.mark.django_db
def test_create_incorrect_input(api_client, default_user):
    api_client.force_authenticate(user=default_user)
    url = reverse("geolocation-list")
    response = api_client.post(url, data={'ip_or_url': 'test_url'})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["detail"][0] == "Please provide a correct IP address or URL starting with www."


@pytest.mark.django_db
def test_create(api_client, default_user, geolocation_dict):
    api_client.force_authenticate(user=default_user)
    url = reverse("geolocation-list")
    from unittest import mock
    with mock.patch('api.views.call_ipstack', return_value=geolocation_dict):
        response = api_client.post(url, data={'ip_or_url': '213.135.155.90'})
        assert response.status_code == status.HTTP_201_CREATED
        assert Geolocation.objects.filter(ip=geolocation_dict['ip']).exists()

