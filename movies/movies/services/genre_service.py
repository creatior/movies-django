from typing import Dict, Any
from movies.models.genre import Genre


def list_genres(filters: Dict[str, Any]):
    queryset = Genre.objects.all()

    if filters.get("name"):
        queryset = queryset.filter(name__icontains=filters["name"])

    return queryset
