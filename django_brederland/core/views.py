from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.views import generic

from .models import Municipality, VisitedMunicipality

class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'top_municipality_list'

    def get_queryset(self):
        """
        Return the existing municipalities

        note: order_by('?') is known to be slow
        """
        return Municipality.objects.order_by('?')[:4]

class ProvinceView(generic.ListView):
    template_name = 'core/provincie.html'
    context_object_name = 'province_municipality_list'
    
    def get_queryset(self):
        """
        Fetches province name 
        Parses it in correct format (e.g. noord-brabant --> Noord-Brabant)
        Returns the municipalities that belong to the 
        province 'province_label'
        """
        province_label = self.kwargs['province']
        split = province_label.split('-')
        province_label_fin = None

        for word in split:
            if province_label_fin is None:
                province_label_fin = word.capitalize()
            else: 
                province_label_fin = province_label_fin + '-' + word.capitalize()

        return Municipality.objects.filter(province=province_label_fin).order_by('label')

class MunicipalityView(generic.DetailView):
    template_name = 'core/gemeente.html'

    def get_object(self):
        cbs_code_mun = self.kwargs['cbs_code'] 
        print(cbs_code_mun)
        return get_object_or_404(Municipality, cbs_code=cbs_code_mun)