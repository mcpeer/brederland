# Generated by Django 2.1.4 on 2019-01-17 13:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20190117_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipalitylist',
            name='source_description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='municipalitylist',
            name='source_url',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='municipalitylist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 13, 43, 16, 961824, tzinfo=utc), verbose_name='date published'),
        ),
    ]
