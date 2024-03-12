from django.urls import path
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about_us'),
    path('price/', views.price, name='price'),
    path('service/', views.service, name='service'),
]