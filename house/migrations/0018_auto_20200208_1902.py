# Generated by Django 3.0.3 on 2020-02-08 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0008_city_timezone'),
        ('house', '0017_auto_20200129_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Region'),
        ),
    ]
