from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('provincie/<str:province>/', views.ProvinceView.as_view(), name='province'),
    path('gemeente/<str:cbs_code>/', views.MunicipalityView.as_view(), name='municipality'),
    # path('account/', include('django.contrib.auth.urls')), # new
]