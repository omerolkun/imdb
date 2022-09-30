from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='movies'),
        path('actors/', views.actors, name='actors'),
        path('<int:para>', views.single_movie, name='single movie'),
]
