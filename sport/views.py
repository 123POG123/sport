from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView
from .form import FormMyForm

class HomePageView(TemplateView):
    #home page
    template_name = 'sport/home.html'


class AboutPageView(TemplateView):
    #about page
    template_name = 'sport/about_us.html'


class BlogPageView(TemplateView):
    #blog page
    template_name = 'sport/blog.html'


class ContactPageView(TemplateView):
    #contact page
    template_name = 'sport/contact.html'

class ServicesPageView(TemplateView):
    #services page
    template_name = 'sport/services.html'

