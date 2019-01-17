# load the necessary files to connect to db
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_brederland.settings")
import django
django.setup()

# import json
import json

# Django models
from core.models import Municipality, MunicipalityList, MunicipalityListMembership, MunicipalityListType

def write_municipality_list_membership(list_category, list_name, municipalities):
    """
    Creates List Type instance if that does not exist yet
    Creates List instance with label = list_name 
    and then creates list memberships for every 
    passed municipality in municipalities
    """

    t = MunicipalityListType.objects.filter(label=list_category)

    if len(t) == 0:
        # create new List Type
        t = MunicipalityListType()
        t.label = list_category
        t.save()
    elif len(t) == 1:
        t = t[0]
    else:
        return 'This is not normal, there are multiple lists with this name'

    m = MunicipalityList.objects.filter(label=list_name)
    if len(m) ==0:
        # create a new List
        m = MunicipalityList()
        m.label = list_name
        m.category = t
        # m.pub_date is set automatically to now.
        m.save()
    else: 
        return 'The list already exists with this name, abort'
    
    # else we go on and add new memberships 
    for municipality in municipalities:
        n = MunicipalityListMembership()
        n.municipality = municipality
        n.list_membership = m
        n.save()
    
    return 'done with' + list_name

if __name__ == '__main__':   
    # load all current municipalities
    municipalities = Municipality.objects.all()
    
    # now we make a list with ALL municipalities = NL and for every province. 

    # create nederland list
    # write_municipality_list_membership('Regionale indeling', 'Nederland', municipalities)

    provinces = list(set(Municipality.objects.all().values_list('province', flat=True)))

    for province in provinces:
        province_municipalities = Municipality.objects.filter(province = province)
        output = write_municipality_list_membership('Regionale indeling', province, province_municipalities)