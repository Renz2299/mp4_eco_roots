from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact_review/', views.contact_review, name='contact_review'),
    path('about/', views.about, name='about'),
    path('delivery/', views.delivery, name='delivery'),
    path('privacy/', views.privacy, name='privacy'),
]
