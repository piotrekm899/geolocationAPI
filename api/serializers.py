from rest_framework import serializers
from .models import (
    Connection,
    Currency,
    Geolocation,
    Language,
    Location,
    Security,
    TimeZone,
)

from .validators import validate_ip, validate_url


class IPURLSerializer(serializers.Serializer):
    ip_or_url = serializers.CharField(max_length=200)

    def validate(self, data):
        ip_or_url = data['ip_or_url']
        if not (validate_ip(ip_or_url) or validate_url(ip_or_url)):
            raise serializers.ValidationError(
                {'detail': 'Please provide a correct IP address or URL starting with www.'})
        return data


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)

    class Meta:
        model = Location
        fields = '__all__'


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = '__all__'


class TimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeZone
        fields = '__all__'


class GeolocationSerializer(serializers.ModelSerializer):
    connection = ConnectionSerializer(required=False)
    currency = CurrencySerializer(required=False)
    location = LocationSerializer(required=False)
    security = SecuritySerializer(required=False)
    timezone = TimeZoneSerializer(required=False)

    def create(self, validated_data):
        connection = validated_data.pop('connection', None)
        currency = validated_data.pop('currency', None)
        location = validated_data.pop('location', None)
        security = validated_data.pop('security', None)
        time_zone = validated_data.pop('time_zone', None)
        geolocation, _ = Geolocation.objects.get_or_create(**validated_data)
        if connection:
            conn, _ = Connection.objects.get_or_create(**connection)
            conn.geolocation.add(geolocation)
        if currency:
            curr, _ = Currency.objects.get_or_create(**currency)
            curr.geolocation.add(geolocation)
        if security:
            sec, _ = Security.objects.get_or_create(**security)
            sec.geolocation.add(geolocation)
        if time_zone:
            tz, _ = TimeZone.objects.get_or_create(**time_zone)
            tz.geolocation.add(geolocation)
        if location:
            languages = location.pop('languages', None)
            loc, _ = Location.objects.get_or_create(**location)
            loc.geolocation.add(geolocation)
            if languages:
                for language in languages:
                    lang, _ = Language.objects.get_or_create(**language)
                    loc.languages.add(lang)
        return geolocation

    class Meta:
        model = Geolocation
        fields = '__all__'

