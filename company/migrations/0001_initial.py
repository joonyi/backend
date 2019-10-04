# Generated by Django 2.2 on 2019-10-03 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('company_logo', models.CharField(blank=True, max_length=200, null=True)),
                ('cb_name', models.CharField(max_length=200, null=True)),
                ('cb_company_logo', models.CharField(blank=True, max_length=200, null=True)),
                ('cb_domain', models.CharField(max_length=50, null=True)),
            ],
            options={
                'ordering': ['company'],
            },
        ),
    ]
