from django.contrib import admin
from movies.models.models import Movie, Genre, Director

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
