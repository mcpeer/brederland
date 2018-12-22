from django.db import models

# Create your models here.

# change below to match 'Municipality' and 'VisitedMunicipality' 
import uuid

from django.db import models
from django.contrib.auth import get_user_model


class Municipality(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    flag_image_url = models.CharField(max_length=255, null=True)
    cbs_code = models.CharField(max_length=4)

    def __str__(self):
        return self.label


class VisitedMunicipality(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    municipality = models.ForeignKey(
        'Municipality',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    issued_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} visited by {1}".format(str(self.municipality), str(self.user))