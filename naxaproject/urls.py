
from django.contrib import admin
from django.urls import path
from project_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('excel/', views.ReadExcelCreateApiView.as_view(), name='excel'),
    path('excel/list', views.ReadExcelListApiView.as_view(), name='excel-list'),
    path('excel/filter', views.ReadExcelFilterApiView.as_view(), name='excel-list'),
    path('excel/municipality', views.ReadExcelMunicipalityApiView.as_view(), name='excel-list')
]
