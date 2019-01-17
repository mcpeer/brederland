from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from .models import Municipality, VisitedMunicipality, Province, MunicipalityListMembership
from django.contrib.auth.models import User

import json 

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

        # load the simplified province JSON
        province = Province.objects.filter(label=province_label_fin)[0]

        # Here I try to return a list, this works. 
        return [Municipality.objects.filter(province=province_label_fin).order_by('label'),province]

# class ProvinceView(generic.ListView):
#     template_name = 'core/provincie.html'
#     context_object_name = 'province_municipality_list'
    
#     def get_queryset(self):
#         """
#         Fetches province name 
#         Parses it in correct format (e.g. noord-brabant --> Noord-Brabant)
#         Returns the municipalities that belong to the 
#         province 'province_label'
#         """
#         province_label = self.kwargs['province']
#         split = province_label.split('-')
#         province_label_fin = None

#         for word in split:
#             if province_label_fin is None:
#                 province_label_fin = word.capitalize()
#             else: 
#                 province_label_fin = province_label_fin + '-' + word.capitalize()

#         province_municipality_list = Municipality.objects.filter(province=province_label_fin).order_by('label')

#         # parse all shapefiles to one big multipolygon    
#         total_shapefile = 

#         return {'province_municipality_list': province_municipality_list, 'province_shapes': total_shapefile}

class MunicipalityView(generic.DetailView):
    template_name = 'core/gemeente.html'

    def get_object(self):
        cbs_code_mun = self.kwargs['cbs_code'] 
        print(cbs_code_mun)
        return get_object_or_404(Municipality, cbs_code=cbs_code_mun)

class DashboardView(generic.ListView):
    template_name = 'core/dashboard.html'
    context_object_name = 'user_information'

    def get_queryset(self):
        """
        Return the number of municipalities that 
        this user has visited.
        """

        list_of_visited_municipalities = VisitedMunicipality.objects.filter(
            user_id=self.request.user.id).order_by('-issued_date')[:10]

        nr_visits = len(list_of_visited_municipalities)

        return [list_of_visited_municipalities, nr_visits]

class DashboardProfileView(generic.UpdateView):
    template_name = 'core/dashboard-my-profile.html'
    model = User
    fields = ['first_name', 'last_name', 'email']

    success_url = reverse_lazy('core:dashboard-profile')

    def get_object(self, queryset=None):
        return self.request.user


class DashboardNLListView(generic.ListView):
    model = VisitedMunicipality
    fields = ['municipality']
    context_object_name = 'list_information'

    success_url=reverse_lazy('core:dashboard-nl-list')

    def get_queryset(self):
        list_label = 'Nederland'

        list_of_visited_municipalities = VisitedMunicipality.objects.filter(
            user_id=self.request.user.id).values_list('municipality__label', flat=True)
        print(list_of_visited_municipalities)

        all_municipalities = MunicipalityListMembership.objects.filter(
            list_membership__label = list_label).order_by('municipality__label')
        #all_municipalities = Municipality.objects.all().order_by('label')

        complete = round(len(list_of_visited_municipalities)/len(all_municipalities)*100)
        
        print(all_municipalities)
        return [list_of_visited_municipalities, all_municipalities, complete, list_label]

    def form_valid(self, form):
        form.instance.user_id = self.request.user.ids
        return super(DashboardNLListView, self).form_valid(form)

    template_name = 'core/dashboard-nl-list.html'

