from django.db import models


class Geolocation(models.Model):
    ip = models.CharField(max_length=50)
    type = models.CharField(max_length=4)
    continent_code = models.CharField(max_length=2)
    continent_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=50)
    region_code = models.CharField(max_length=3)
    region_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=8)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, related_name='geolocation', null=True,)
    currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, related_name='geolocation', null=True,)
    connection = models.ForeignKey('Connection', on_delete=models.SET_NULL, related_name='geolocation', null=True,)
    security = models.ForeignKey('Security', on_delete=models.SET_NULL, related_name='geolocation', null=True,)
    timezone = models.ForeignKey('TimeZone', on_delete=models.SET_NULL, related_name='geolocation', null=True,)

    def __str__(self):
        return f"{self.ip}"


class Location(models.Model):
    geoname_id = models.IntegerField()
    capital = models.CharField(max_length=50)
    languages = models.ManyToManyField('Language')
    country_flag = models.URLField()
    country_flag_emoji = models.TextField()
    country_flag_emoji_unicode = models.CharField(max_length=255)
    calling_code = models.CharField(max_length=2)
    is_eu = models.BooleanField()

    def __str__(self):
        return f"{self.geoname_id}"


class Language(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    native = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code}"


class TimeZone(models.Model):
    db_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    current_time = models.DateTimeField()
    gmt_offset = models.IntegerField()
    code = models.CharField(max_length=3)
    is_daylight_saving = models.BooleanField()

    def __str__(self):
        return f"{self.current_time}"


class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    plural = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5)
    symbol_native = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code}"

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Connection(models.Model):
    asn = models.IntegerField()
    isp = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.asn}"


class Security(models.Model):
    is_proxy = models.BooleanField()
    proxy_type = models.CharField(max_length=3, null=True)
    is_crawler = models.BooleanField()
    crawler_name = models.CharField(max_length=50, null=True)
    crawler_type = models.CharField(max_length=50, null=True)
    is_tor = models.BooleanField()
    threat_level = models.CharField(max_length=6)
    threat_types = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Security"
        verbose_name_plural = "Securities"

