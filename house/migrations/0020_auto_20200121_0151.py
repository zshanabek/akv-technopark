# Generated by Django 2.2.7 on 2020-01-20 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0008_city_timezone'),
        ('house', '0019_auto_20200117_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
        ),
    ]