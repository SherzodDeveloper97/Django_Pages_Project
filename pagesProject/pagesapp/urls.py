from django.urls import path
from .views import HomePageView, AboutPageView, ServicePageView, ContactPageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('service/',ServicePageView.as_view(),name='service'),
    path('contact/',ContactPageView.as_view(),name='contact')
]