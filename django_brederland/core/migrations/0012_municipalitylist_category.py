# Generated by Django 2.1.4 on 2019-01-17 09:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190117_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipalitylist',
            name='category',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='core.MunicipalityListType'),
        ),
    ]
