from movies.models.movie import Movie

def list_movies(filters=None):
    queryset = Movie.objects.all()

    if filters is None:
        filters = {}
    
    title = filters.get("title")
    year = filters.get("release_year")

    if title:
        queryset = queryset.filter(title=title)
    if year:
        queryset = queryset.filter(release_year=year)
    return queryset