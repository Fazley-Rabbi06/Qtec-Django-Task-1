# Generated by Django 3.2 on 2021-04-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Main', '0002_parcel_parcel_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='parcel_cod_charge',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parcel',
            name='parcel_return_charge',
            field=models.IntegerField(default=0),
        ),
    ]
