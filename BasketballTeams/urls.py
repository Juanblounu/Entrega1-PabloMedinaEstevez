from django.urls import path
from .views import home_page, create_team, about_me, edit_team, show_team
from . import views


urlpatterns = [
    path('', home_page, name='index'),
    path('teams/', views.TeamsList.as_view(), name='teams_list'),
    path('create-team/', create_team, name='create_team'),
    path('edit-team/<int:id>/', edit_team, name='edit_team'),
    path('delete-team/<int:pk>/', views.DeleteTeam.as_view(), name='delete_team'),
    path('show-team/<int:id>/', show_team, name='show_team'),
    path('about-me/', about_me, name='about_me'),
]    