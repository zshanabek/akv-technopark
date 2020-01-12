# Generated by Django 2.2.7 on 2020-01-12 18:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messagemodel',
            options={'ordering': ('-created_at',), 'verbose_name': 'message', 'verbose_name_plural': 'messages'},
        ),
        migrations.RemoveField(
            model_name='messagemodel',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 1, 12, 18, 13, 0, 721158, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='body',
            field=models.TextField(max_length=2000),
        ),
    ]
