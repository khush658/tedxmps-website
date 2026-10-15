from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore-events/', views.explore_events, name='explore_events'),
    path('speakers/', views.speakers, name='speakers'),
    path('about/', views.about, name='about'),
    path('guidelines/', views.guidelines, name='guidelines')
]