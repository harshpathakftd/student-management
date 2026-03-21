from django.urls import path
from . import views

urlpatterns = [
    path('download-excel/', views.download_report, name='download_report'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
]