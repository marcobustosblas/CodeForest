# Generated by Django 4.1.5 on 2023-04-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="users", verbose_name="Imagen de Perfil"
            ),
        ),
    ]
