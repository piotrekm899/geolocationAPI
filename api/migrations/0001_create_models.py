# Generated by Django 3.0 on 2020-11-26 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asn', models.IntegerField()),
                ('isp', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('plural', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=5)),
                ('symbol_native', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('native', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_proxy', models.BooleanField()),
                ('proxy_type', models.CharField(max_length=3, null=True)),
                ('is_crawler', models.BooleanField()),
                ('crawler_name', models.CharField(max_length=50, null=True)),
                ('crawler_type', models.CharField(max_length=50, null=True)),
                ('is_tor', models.BooleanField()),
                ('threat_level', models.CharField(max_length=6)),
                ('threat_types', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Security',
                'verbose_name_plural': 'Securities',
            },
        ),
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('db_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=50)),
                ('current_time', models.DateTimeField()),
                ('gmt_offset', models.IntegerField()),
                ('code', models.CharField(max_length=3)),
                ('is_daylight_saving', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geoname_id', models.IntegerField()),
                ('capital', models.CharField(max_length=50)),
                ('country_flag', models.URLField()),
                ('country_flag_emoji', models.TextField()),
                ('country_flag_emoji_unicode', models.CharField(max_length=255)),
                ('calling_code', models.CharField(max_length=2)),
                ('is_eu', models.BooleanField()),
                ('languages', models.ManyToManyField(to='api.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=4)),
                ('continent_code', models.CharField(max_length=2)),
                ('continent_name', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=2)),
                ('country_name', models.CharField(max_length=50)),
                ('region_code', models.CharField(max_length=3)),
                ('region_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=8)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('connection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geolocation', to='api.Connection')),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geolocation', to='api.Currency')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geolocation', to='api.Location')),
                ('security', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geolocation', to='api.Security')),
                ('timezone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geolocation', to='api.TimeZone')),
            ],
        ),
    ]