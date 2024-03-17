from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.

def index(request):

    movies = Movie.objects.all()
    #SELECT * FROM movies_movie
    #output = ', '.join([m.title for m in movies])


    # Movie.objects.filter(release_year=1984)
    # SELECT * FROM movies_movie WHERE release_year = 1984

    # Movie.objects.get(id=1)
    # Single Object get
    # Additionally we could use Raw SQL Statements 

    #return HttpResponse(output)
    return render(request, 'movies/index.html',{'movies': movies})