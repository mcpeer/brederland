from django.shortcuts import render

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