import requests

from django.conf import settings
from .exceptions import IPStackException


def call_ipstack(ip_or_url):
    url = "http://api.ipstack.com/" + ip_or_url
    payload = {"access_key": settings.IP_STACK_ACCESS_KEY}
    response = requests.get(url, params=payload)
    r_json = response.json()
    if r_json.get('success', None) is False:
        raise IPStackException(r_json['error'])
    return r_json

