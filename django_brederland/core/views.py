from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy,reverse

from .models import Municipality, VisitedMunicipality, Province, MunicipalityListMembership, MunicipalityList, MunicipalityListType, ResidenceMap
from django.contrib.auth.models import User
from django.utils import timezone

import json 
from django.http import JsonResponse


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

        nr_visits = VisitedMunicipality.objects.filter(
            user_id=self.request.user.id).count()


        return [list_of_visited_municipalities, nr_visits]

class DashboardProfileView(generic.UpdateView):
    template_name = 'core/dashboard-my-profile.html'
    model = User
    fields = ['first_name', 'last_name', 'email']

    success_url = reverse_lazy('core:dashboard-profile')

    def get_object(self, queryset=None):
        return self.request.user

class DashboardListView(generic.ListView):
    model = VisitedMunicipality
    context_object_name = 'list_information'
    template_name = 'core/dashboard-list.html'

    def get_queryset(self):
        """
        Retrieve visited municipalities for user
        Retrieve all municipalities that are in this list 
        Calculate completion metric
        return both to the page. 
        """
        pk = self.kwargs.get('pk')

        list_label = get_object_or_404(MunicipalityList, id=pk)

        all_municipalities_from_list = MunicipalityListMembership.objects.filter(
            list_membership__id = pk).order_by('municipality__label')

        list_of_visited_municipalities = VisitedMunicipality.objects.filter(
            user_id=self.request.user.id, municipality__label__in=all_municipalities_from_list.values_list('municipality__label')).values_list('municipality__label', flat=True)

        complete = round(len(list_of_visited_municipalities)/len(all_municipalities_from_list)*100)
        
        return [list_of_visited_municipalities, all_municipalities_from_list, complete, list_label]

def update_visited(request, pk):
    # pk is the list that we will alter
    municipalities_in_list = MunicipalityListMembership.objects.filter(list_membership__id=pk)

    # delete all checked by user 
    VisitedMunicipality.objects.filter(
        user_id = request.user.id, municipality__label__in=municipalities_in_list.values_list('municipality__label')).delete()
    
    checked = request.POST.getlist('check')
    print(checked)

    # create newly checked by user
    if len(checked) > 0:
        for municipality_id in checked:
            m = VisitedMunicipality()
            m.municipality = get_object_or_404(Municipality, id=municipality_id)
            m.user = request.user
            m.issued_date = timezone.now()
            m.save()

    return HttpResponseRedirect(reverse('core:dashboard-single-list', args=(pk,)))
   

class DashboardListsView(generic.ListView):
    template_name = 'core/dashboard-lists.html'
    model = MunicipalityList
    context_object_name = 'lists_information'

    def get_queryset(self):
        """
        Return the lists available on the website.
        """
        list_types = MunicipalityListType.objects.all().order_by('label')
        
        result = []
        for i in list_types:
            result.append(MunicipalityList.objects.filter(category = i).order_by('label'))

        return result

def autocomplete(request):
    if request.is_ajax():
        queryset = ResidenceMap.objects.filter(city_name__contains=request.GET.get('search', None))
        print(queryset)

        list = []        
        for i in queryset:
            list.append(str(i.city_name)+' ('+str(i.municipality)+')')
        data = {
            'list': list,
        }
        return JsonResponse(data)