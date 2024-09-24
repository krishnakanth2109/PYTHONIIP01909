from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dynamic/', views.dynamic_content, name='dynamic_content'),
    path('form/', views.contact_form, name='contact_form'),
    path('submit/', views.submit_form, name='submit_form'),
    path('submit/', views.submit, name='submit'), 
]
