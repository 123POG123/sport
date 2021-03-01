from django.urls import path
from .views import HomePageView


urlpatterns = [
    path('sport/', HomePageView.as_view(), name='sport_home'),
]
