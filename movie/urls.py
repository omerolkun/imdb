from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='movies'),
        path('actors/', views.actors, name='actors'),
        path('<int:para>', views.single_movie, name='single_movie'),
        path('directors/', views.directors, name='directors'),
        path('directors/<int:pawra>', views.single_director, name='single_director'),
        path('actors/<int:param>', views.single_actor, name='single_actor')
]

