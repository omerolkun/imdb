from django.shortcuts import render
from .models import Movie, Actor,Movie_Director, Movie_Actor
# Create your views here.

def home(request):
    movie_list =list( Movie.objects.all() )
    m = movie_list[0]
    print(m)
    context = { 'movlist' : movie_list,'iteration':range(0,38)}
    return render(request, 'movie/movies.html', context )

def single_movie(request, para):
    movie = Movie.objects.all()[para-1]
    director = Movie_Director.objects.get(movie_id = para )
    actors = Movie_Actor.objects.filter(movie_id = para) 
    print("actors are 0> ", actors)
    print("director objects -> " , director)
    return render(request, 'movie/singlemovie.html', {'para':movie, 'director':director, "actors":actors})

def actors(request):
    actor_list = list( Actor.objects.all() )
    context = { 'actlist' : actor_list , }
    return render (request, 'movie/actors.html', context)
