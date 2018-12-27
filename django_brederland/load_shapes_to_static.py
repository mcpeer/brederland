# load the necessary files to connect to db
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_brederland.settings")
import django
django.setup()

import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# import json
import json

# Django models
from core.models import Municipality
from collections import OrderedDict


if __name__ == '__main__':       
    # load the shapefiles
    with open('data/geojson/raw/convert2.json', encoding='utf-8') as f:
        geo_json = json.load(f, object_pairs_hook=OrderedDict)

    max_len = 0
    # parse db inputs
    for shape in geo_json['features']:
        filename = shape['properties']['code']+'.json'
        print(shape.keys())
        if max_len < len(str(shape)):
            max_len = len(str(shape))
        # Write JSON file
        with io.open('core/static/core/geos/'+filename, 'w', encoding='utf8') as outfile:
            str_ = json.dumps(shape
            # ,
            #                 indent=4, sort_keys=False,
            #                 separators=(',', ': '), ensure_ascii=False
            )
            outfile.write(to_unicode(str_))    
    
    print(max_len)