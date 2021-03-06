# Generated by Django 3.0.3 on 2020-02-26 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0018_auto_20200208_1902'),
        ('reservation', '0012_auto_20200222_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='house.House'),
        ),
    ]
