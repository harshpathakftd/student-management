from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),

    path('add/', views.add_payment, name='add_payment'),

    path('mark-paid/<int:id>/', views.mark_paid, name='mark_paid'),
]