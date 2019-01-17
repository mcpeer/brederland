from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('provincie/<str:province>/', views.ProvinceView.as_view(), name='province'),
    path('gemeente/<str:cbs_code>/', views.MunicipalityView.as_view(), name='municipality'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard-profile', views.DashboardProfileView.as_view(), name='dashboard-profile'),
    path('dashboard-lists', views.DashboardListsView.as_view(), name='dashboard-lists'),
    path('dashboard-list/<uuid:pk>/', views.DashboardListView.as_view(), name='dashboard-single-list'),
    
    # path to update the visited municipalities
    path('update-municipalities/<uuid:pk>', views.update_visited, name='update-visited'),  

    # path('account/', include('django.contrib.auth.urls')), # new
]