# load the necessary files to connect to db
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_brederland.settings")
import django
django.setup()

# import pandas
import pandas as pd

# Django models
from core.models import Municipality, ResidenceMap

def write_residence_map(woonplaats_name, woonplaats_code, gemeente_code):
    """
    """
    try:
        r = ResidenceMap()
        r.city_code = woonplaats_code
        r.city_name = woonplaats_name
        municipality = Municipality.objects.filter(cbs_code = gemeente_code)[0]
        r.municipality = municipality
        r.save()
        return True

    except Exception as e:
        print(e)
        print('we did not find the municipality with cbs code ', gemeente_code, woonplaats_name)
        return False

if __name__ == '__main__':   
    # delete current ResidenceMaps
    ResidenceMap.objects.all().delete()

    # # open file with places of residence:
    data = pd.read_csv('data/cbs_woonplaatsen_2018/Woonplaatsen_in_Nederland_2018_17012019_124959.csv', sep=";")
    data.columns = ['woonplaats', 'woonplaats_code', 'gemeentenaam', 'gemeentecode']
    data['woonplaats_code'] = data['woonplaats_code'].apply(lambda x: x.replace(' ', ''))
    data['gemeentecode'] = data['gemeentecode'].apply(lambda x: x[2:].replace(' ', ''))

    for row in data.itertuples():
        success = write_residence_map(
            woonplaats_name=row.woonplaats, woonplaats_code=row.woonplaats_code, gemeente_code=row.gemeentecode)
        if success:
            print(str(ResidenceMap.objects.filter(city_code = row.woonplaats_code)[0]).encode("latin-1"))

    # all are successfully loaded. 