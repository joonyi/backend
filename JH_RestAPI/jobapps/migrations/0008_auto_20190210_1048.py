# Generated by Django 2.1.5 on 2019-02-10 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapps', '0007_auto_20190210_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statushistory',
            name='application_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jobapps.ApplicationStatus'),
        ),
    ]
