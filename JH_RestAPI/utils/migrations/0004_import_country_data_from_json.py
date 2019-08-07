# Generated by Django 2.1.5 on 2019-04-23 06:39

import json
import urllib

from django.db import migrations


class Migration(migrations.Migration):

    def populate_data(apps, schema_editor):
        Country = apps.get_model('utils', 'Country')
        State = apps.get_model('utils', 'State')
        with urllib.request.urlopen("https://raw.githubusercontent.com/stefanbinder/countries-states/master/countries.json") as json_file:
            data = json.load(json_file)
            for d in data:
                code2 = d['code2']
                code3 = d['code3']
                name = d['name']
                capital = d['capital']
                region = d['region']
                subregion = d['subregion']
                country = Country.objects.create(code2=code2,code3=code3,name=name,capital=capital,region=region,subregion=subregion)
                country.save()
                for w in d['states']:
                    code = w['code']
                    if code is None:
                        code = ''
                    name = w['name']
                    subdivision = w['subdivision']
                    if subdivision is None:
                        subdivision = ''
                    state = State.objects.create(country=country, code=code, name=name, subdivision=subdivision)
                    state.save()
                
    dependencies = [
        ('utils', '0003_remove_country_states'),
    ]

    operations = [
        migrations.RunPython(populate_data, reverse_code=migrations.RunPython.noop)
    ]
