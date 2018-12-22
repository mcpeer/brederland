# load the necessary files to connect to db
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_brederland.settings")
import django
django.setup()

# import json
import json

# Django models
from core.models import Municipality

def write_municipality(muni_dict):
    """
    Input:
    {
        'label': 'Utrecht', 
        'province': 'Utrecht',
        'flag_image_url: 'http://...',
        'cbs_code': '1111'
    }

    Takes input and saves it in the DB.
    """
    m = Municipality()
    m.label = muni_dict['label']
    m.province = muni_dict['province']
    m.flag_image_url = muni_dict['flag_image_url']
    m.cbs_code = muni_dict['cbs_code']
    m.save()


if __name__ == '__main__':   
    # delete current municipalities 
    municipalities = Municipality.objects.all().delete()
    
    # load the municipalities
    with open('data/processed/query_result.json', encoding='utf-8') as f:
        municipality_dict = json.load(f)
    
    # parse db inputs
    for m in municipality_dict:
        input_format = {
            'label': m['muniLabel'],
            'province': m['provinceLabel'],
            'cbs_code': m['CBS_munici_code']
        }

        if 'flag_image' in m.keys():
            input_format['flag_image_url'] = m['flag_image']
        else: 
            input_format['flag_image_url'] = None

        write_municipality(input_format)    