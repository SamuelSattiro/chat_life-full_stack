from django.apps import AppConfig
import os

print("🔥 users.apps carregado")

class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        print("🔥 ready() executado")
        if os.environ.get("CREATE_SUPERUSER") != "true":
            return

        from django.contrib.auth import get_user_model

        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "samuel")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "samuelsattiro.dev@gmail.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "Cami1808")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            print("✔ Superuser criado automaticamente")
        else:
            print("ℹ Superuser já existe")