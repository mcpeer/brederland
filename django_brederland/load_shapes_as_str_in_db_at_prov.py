# load the necessary files to connect to db
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_brederland.settings")
import django
django.setup()

# import json
import json

import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
    
from collections import OrderedDict

# Django models
from core.models import Municipality, Province

def get_all_municipality_codes(query_result):
    """ takes query result and returns list of cbs codes """
    code_list = []
    for q in query_result:
        code_list.append(q.cbs_code)
    return code_list

def write_province(label_name, str_geo_json):
    """
    Takes input and saves it in the DB.
    """
    p = Province()
    p.label = label_name
    p.multi_polygon = to_unicode(str_geo_json)
    p.save()
    

if __name__ == '__main__':   
    # get list of unique provinces: 
    provinces = ['Drenthe', 'Noord-Holland', 'Utrecht', 'Gelderland',
                    'Limburg', 'Noord-Brabant', 'Overijssel', 'Zeeland',
                        'Zuid-Holland', 'Groningen', 'Flevoland', 'Friesland']

    for prov in provinces:
        # load the shapefiles
        with open('data/geojson/raw/convert2.json', encoding='utf-8') as f:
            geo_json = json.load(f, object_pairs_hook=OrderedDict)

        ms = Municipality.objects.filter(province=prov).order_by('label')
        m_code_list = get_all_municipality_codes(ms)

        filter_result = []
        for shape in geo_json['features']:
            if shape['properties']['code'] in m_code_list:
                filter_result.append(shape)

        geo_json['features'] = filter_result

        str_ = json.dumps(geo_json)
        write_province(prov, str_)
