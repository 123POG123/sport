from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView


class HomePageView(TemplateView):
    template_name = 'sport/home.html'