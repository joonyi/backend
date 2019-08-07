# Generated by Django 2.1.5 on 2019-02-10 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapps', '0009_auto_20190210_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='applicationStatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='jobapplication_applicationStatus', to='jobapps.ApplicationStatus'),
        ),
        migrations.AlterField(
            model_name='statushistory',
            name='application_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='statushistory_applicationStatus', to='jobapps.ApplicationStatus'),
        ),
    ]
