# Generated by Django 4.1.5 on 2023-04-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="USER",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=90, unique=True, verbose_name="Nombre de Usuario"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="Email"
                    ),
                ),
                ("password", models.CharField(max_length=70)),
                (
                    "image",
                    models.ImageField(
                        upload_to="users", verbose_name="Imagen de Perfil"
                    ),
                ),
            ],
        ),
    ]
