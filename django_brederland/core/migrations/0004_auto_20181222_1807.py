# Generated by Django 2.1.4 on 2018-12-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181222_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='cbs_code',
            field=models.CharField(max_length=4),
        ),
    ]
