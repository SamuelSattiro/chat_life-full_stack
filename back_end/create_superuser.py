import os
import django

from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back_end.settings")
django.setup()


User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="samuel",
        email="samuelsattiro.dev@gmail.com",
        password="Cami1808"
    )
    print("Superuser criado com sucesso")
else:
    print("Superuser já existe")