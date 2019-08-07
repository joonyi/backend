# Generated by Django 2.2 on 2019-08-05 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0004_import_country_data_from_json'),
        ('users', '0027_auto_20190804_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.Country'),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.State'),
        ),
    ]
