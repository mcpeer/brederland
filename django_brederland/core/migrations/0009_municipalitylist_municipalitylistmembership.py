# Generated by Django 2.1.4 on 2019-01-17 09:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='MunicipalityList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='MunicipalityListMembership',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('list_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.MunicipalityList')),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Municipality')),
            ],
        ),
    ]