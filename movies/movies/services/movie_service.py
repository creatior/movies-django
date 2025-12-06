from movies.models.movie import Movie

def list_movies(filters=None):
    queryset = Movie.objects.all()

    if filters is None:
        filters = {}
    
    title = filters.get("title")
    year = filters.get("release_year")
    director_id = filters.get("director_id")
    genre_ids = filters.get("genre_ids")

    if title:
        queryset = queryset.filter(title__icontains=title)
    if year:
        queryset = queryset.filter(release_year=year)
    if director_id:
        queryset = queryset.filter(director_id=director_id)
    if genre_ids:
        genre_ids = [int(g) for g in genre_ids]
        for genre_id in genre_ids:
            queryset.filter(genres__id=genre_id)
        queryset.distinct()

    return queryset.select_related("director").prefetch_related("genres")