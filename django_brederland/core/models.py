from django.db import models
import datetime

# Create your models here.

# change below to match 'Municipality' and 'VisitedMunicipality' 
import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Municipality(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    flag_image_url = models.CharField(max_length=255, null=True)
    cbs_code = models.CharField(max_length=4)
    multi_polygon_str = models.CharField(max_length=400000, null=True)

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

class Province(models.Model):
    """
    Province class. Actually, Municipality should be linked to this.
    However, this can also be done via MunicipalityLists object below. 
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)
    multi_polygon = models.CharField(max_length=150000000, null=True)

    def __str__(self):
        return self.label

class MunicipalityListType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    label = models.CharField(max_length = 500)

    def __str__(self):
        return self.label


class MunicipalityList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    label = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    category = models.ForeignKey(MunicipalityListType, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.label


class MunicipalityListMembership(models.Model):
    """
    This datamodel contains all existing list memberships of all municipalities
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    municipality = models.ForeignKey(Municipality, on_delete = models.CASCADE)
    list_membership = models.ForeignKey(MunicipalityList, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} is in {1}".format(str(self.municipality), str(self.list_membership))

class ResidenceMap(models.Model):
    """
    This datamodel contains all existing residences 
    and maps to province and municipality
    """
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    city_name = models.CharField(max_length = 200)
    city_code = models.CharField(max_length = 6)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0} lies in {1}".format(str(self.city_name), str(self.municipality))