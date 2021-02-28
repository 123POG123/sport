from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView
from .form import FormMyForm

class HomePageView(TemplateView):
    template_name = 'sport/home.html'


class AboutPageView(TemplateView):
    template_name = 'sport/about_us.html'


class BlogPageView(TemplateView):
    template_name = 'sport/blog.html'


class ContactPageView(TemplateView):
    template_name = 'sport/contact.html'

class ServicesPageView(TemplateView):
    template_name = 'sport/services.html'

