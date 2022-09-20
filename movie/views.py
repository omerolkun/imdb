from django.shortcuts import render
from .models import Movie
# Create your views here.

def home(request):
    movie_list =list( Movie.objects.all() )
    m = movie_list[0]
    print(m)
    context = { 'movlist' : movie_list,}
    return render(request, 'movie/movies.html', context )

