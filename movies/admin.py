from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')


class MovieAdmin(admin.ModelAdmin):
    fields = ('title','number_in_stock','daily_rate','release_year','genre')
    list_display = ('title','number_in_stock','daily_rate',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
