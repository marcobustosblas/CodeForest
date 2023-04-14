from django.db import models

# Create your models here. definir tablas, migraciones.

class USER(models.Model):
    username = models.CharField('Nombre de Usuario', unique=True, max_length=90)
    email = models.EmailField('Email', unique=True, max_length=100, blank=False)
    password = models.CharField(max_length=70, blank=False)
    image = models.ImageField('Imagen de Perfil', upload_to='users', blank=True)
    
    def __str__(self):
        return self.username
    
    