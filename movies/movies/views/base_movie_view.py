from rest_framework import viewsets
from rest_framework.permissions import AllowAny

class BaseMovieViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_authenticators(self):
        if self.action in ["list", "retrieve"]:
            return []
        return super().get_authenticators()
    
    def list(self, request):
        raise NotImplementedError("Method list() is not implemented")
    
    def create(self, request):
        raise NotImplementedError("Method create() is not implemented")