from typing import Dict, Any
from movies.models.director import Director


def list_directors(filters: Dict[str, Any]):
    queryset = Director.objects.all()

    if filters.get("full_name"):
        queryset = queryset.filter(full_name__icontains=filters["full_name"])

    return queryset
