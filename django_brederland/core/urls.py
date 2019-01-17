from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('provincie/<str:province>/', views.ProvinceView.as_view(), name='province'),
    path('gemeente/<str:cbs_code>/', views.MunicipalityView.as_view(), name='municipality'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard-profile', views.DashboardProfileView.as_view(), name='dashboard-profile'),
    path('dashboard-nl-list', views.DashboardNLListView.as_view(), name='dashboard-nl-list'),
    # path('account/', include('django.contrib.auth.urls')), # new
]