from django.shortcuts import render
from .models import Movie, Actor
# Create your views here.

def home(request):
    movie_list =list( Movie.objects.all() )
    m = movie_list[0]
    print(m)
    context = { 'movlist' : movie_list,'iteration':range(0,38)}
    return render(request, 'movie/movies.html', context )

#def single_movie(request):
    

def actors(request):
    actor_list = list( Actor.objects.all() )
    context = { 'actlist' : actor_list , }
    return render (request, 'movie/actors.html', context)
