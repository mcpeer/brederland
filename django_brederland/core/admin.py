from django.contrib import admin

from .models import Municipality, VisitedMunicipality, VisitedMunicipality

# class VisitedInLine(admin.TabularInline):
#     model = VisitedMunicipality
#     extra = 3

class MunicipalityAdmin(admin.ModelAdmin):  
    list_filter = ['province']
    search_fields = ['label', 'province']

    list_display = ('label', 'province', 'cbs_code')  
    # inlines = [VisitedInLine] 
    # actually we want this to be inline with the user
    # however we cannot implement this now as we don't have a custom user model. 

# Register your models here.
admin.site.register(Municipality, MunicipalityAdmin)

admin.site.register(VisitedMunicipality)
