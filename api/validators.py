import ipaddress
import re


def validate_ip(ip_or_url):
    try:
        ipaddress.ip_address(str(ip_or_url))
        return True
    except ValueError:
        return False


def validate_url(ip_or_url):
    simple_www_regex = re.compile(r'^(w{3}[.])?[a-z0-9.\-]+[.][a-z]{2,4}$')
    return re.match(simple_www_regex, ip_or_url) is not None


