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
from core.models import Municipality

if __name__ == '__main__':   
    # load the shapefiles
    with open('data/geojson/raw/convert2.json', encoding='utf-8') as f:
        geo_json = json.load(f, object_pairs_hook=OrderedDict)

    # parse db inputs
    for shape in geo_json['features']:
        code = shape['properties']['code']
        name = shape['properties']['gemeentena']
        print(code, name)
        try:
            str_ = json.dumps(shape)

            # find municipality with code in db. 
            m = Municipality.objects.get(cbs_code=code)
            m.multi_polygon_str = to_unicode(str_)
            m.save()

        except:
            print('no instance exists for ', code, name)
