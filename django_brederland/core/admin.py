from django.contrib import admin

from .models import Municipality, VisitedMunicipality, VisitedMunicipality, MunicipalityList, MunicipalityListMembership, MunicipalityListType, ResidenceMap

# class VisitedInLine(admin.TabularInline):,z
#     model = VisitedMunicipality
#     extra = 3

class MunicipalityAdmin(admin.ModelAdmin):  
    list_filter = ['province']
    search_fields = ['label', 'province']

    list_display = ('label', 'province', 'cbs_code')  
    # inlines = [VisitedInLine] 
    # actually we want this to be inline with the user
    # however we cannot implement this now as we don't have a custom user model. 

class MunicipalityListMembershipInLine(admin.TabularInline):
    model = MunicipalityListMembership
    extra = 3

class MunicipalityListAdmin(admin.ModelAdmin):
    list_filter = ['category']
    search_fields = ['label']
    list_display = ('label', 'pub_date', 'category')
    inlines = [MunicipalityListMembershipInLine]

class ResidenceMapAdmin(admin.ModelAdmin):
    list_filter = ['municipality']
    search_fields = ['city_name']

    list_display = ('city_name', 'city_code', 'municipality')

# Register your models here.
admin.site.register(Municipality, MunicipalityAdmin)

admin.site.register(VisitedMunicipality)
admin.site.register(MunicipalityListType)

admin.site.register(MunicipalityList, MunicipalityListAdmin)
admin.site.register(ResidenceMap, ResidenceMapAdmin)
