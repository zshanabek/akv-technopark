# Generated by Django 2.2.7 on 2019-12-09 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_rule_rulehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='description',
            field=models.CharField(default='ok', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='name',
            field=models.CharField(default='house', max_length=255),
            preserve_default=False,
        ),
    ]
