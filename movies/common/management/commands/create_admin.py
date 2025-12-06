from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    help = "Create default Django superuser if it doesn't exist"

    def handle(self, *args, **options):
        username = "admin"
        email = getattr(settings, "DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = getattr(settings, "DJANGO_SUPERUSER_PASSWORD", "admin")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser created: {username} ({email})"))
        else:
            self.stdout.write(f"ℹSuperuser already exists: {username}")