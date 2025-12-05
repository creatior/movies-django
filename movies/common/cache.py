from django.core.cache import cache
import json

def cache_model_instance(*, instance, serializer_class, timeout: int = 300) -> None:
    key = f"{instance.__class__.__name__.lower()}:{instance.id}"
    cache.set(key, json.dumps(serializer_class(instance).data), timeout=timeout)

def get_cached_model(*, model_class, object_id: int) -> dict | None:
    key = f"{model_class.__name__.lower()}:{object_id}"
    data = cache.get(key)
    if data:
        return json.loads(data)
    return None

def delete_cached_model(*, model_class, object_id: int) -> None:
    key = f"{model_class.__name__.lower()}:{object_id}"
    cache.delete(key)