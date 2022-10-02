from django.shortcuts import render
from .models import Movie, Actor,Movie_Director, Movie_Actor, Director
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
    return render(request, 'movie/singlemovie.html', {'para':movie, 'director':director, "actors":actors})


def single_director(request, pawra):
    director = Director.objects.all()[pawra-1]
    movies  = Movie_Director.objects.filter(director_id = pawra)
    return render(request, 'movie/singledirector.html', {'director':director, 'movlist':movies})



def single_actor(request, para):
    actor = Actor.objects.all()[para-1]
    movies = Movie_Actor.objects.filter( actor_id = para ) 
    return render(request, 'movie/singleactor.html', {'actor':actor, 'movlist':movies })





def actors(request):
    actor_list = list( Actor.objects.all() )
    context = { 'actlist' : actor_list , }
    return render (request, 'movie/actors.html', context)
def directors(request):
    return render(request, "movie/directors.html")
