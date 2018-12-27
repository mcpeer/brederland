# the municipalities from the wikiedata query have a few deficiencies: 
# vianen is in there twice. fix: remove the zuidholland vianen. 
# sint oedenrode, schijndel and veghel merged into 'Meierijstad'
# remove these and add Meierijstad. 
#
#
##


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
    # delete Vianen in Zuid-holland
    # Municipality.objects.get(label='Vianen', province='Zuid-Holland').delete()
    
    # create Meijerijstadt
    m_stad = {
        'label': 'Meierijstad', 
        'province': 'Noord-Brabant',
        'flag_image_url': '',
        'cbs_code': '1948'
    }
    #write_municipality(m_stad)

    # delete sint oedenrode, schijndel and veghel
    #unicipality.objects.get(label='Sint-Oedenrode').delete()
    #Municipality.objects.get(label='Schijndel').delete()
    #Municipality.objects.get(label='Veghel').delete()
