# Generated by Django 2.1.4 on 2019-01-17 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190117_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipalitylist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='date published'),
        ),
    ]
