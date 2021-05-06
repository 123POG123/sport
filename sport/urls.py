from django.urls import path
from .views import HomePageView, AboutPageView, BlogPageView, ContactPageView, ServicesPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('services/', ServicesPageView.as_view(), name='services'),
]
