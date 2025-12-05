from django.db import models
from .director import Director
from .genre import Genre

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    release_year = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre, related_name="movies")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.release_year})"