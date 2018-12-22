from django.contrib import admin

from .models import Municipality, VisitedMunicipality

class MunicipalityAdmin(admin.ModelAdmin):  
    list_filter = ['province']
    search_fields = ['label', 'province']

    list_display = ('label', 'province', 'cbs_code')  


# Register your models here.
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(VisitedMunicipality)
