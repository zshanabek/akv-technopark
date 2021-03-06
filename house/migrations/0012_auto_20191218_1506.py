# Generated by Django 2.2.7 on 2019-12-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0011_auto_20191218_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nearbuildinghouse',
            name='house',
        ),
        migrations.RemoveField(
            model_name='nearbuildinghouse',
            name='near_building',
        ),
        migrations.AddField(
            model_name='house',
            name='accommodations',
            field=models.ManyToManyField(to='house.Accommodation'),
        ),
        migrations.AddField(
            model_name='house',
            name='near_buildings',
            field=models.ManyToManyField(to='house.NearBuilding'),
        ),
        migrations.DeleteModel(
            name='AccommodationHouse',
        ),
        migrations.DeleteModel(
            name='NearBuildingHouse',
        ),
    ]
