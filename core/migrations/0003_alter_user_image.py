# Generated by Django 4.1.5 on 2023-04-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="users",
                verbose_name="Imagen de Perfil",
            ),
        ),
    ]
