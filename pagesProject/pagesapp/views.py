from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ServicePageView(TemplateView):
    template_name = 'service.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'