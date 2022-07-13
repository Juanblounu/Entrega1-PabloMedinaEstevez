from django.urls import path
from .views import home_page, teams_list, create_team, about_me


urlpatterns = [
    path('', home_page, name='index'),
    path('teams/', teams_list, name='teams_list'),
    path('create-team/', create_team, name='create_team'),
    path('about-me/', about_me, name='about_me'),
]    