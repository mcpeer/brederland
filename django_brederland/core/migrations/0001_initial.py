# Generated by Django 2.1.4 on 2018-12-22 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('flag_image_url', models.CharField(max_length=255)),
                ('cbs_code', models.IntegerField(default=9999)),
            ],
        ),
        migrations.CreateModel(
            name='VisitedMunicipality',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('issued_date', models.DateTimeField(auto_now=True)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Municipality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
