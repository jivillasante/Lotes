from django.db import models
from django.contrib.auth.models import User

class Lote(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_archivo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='uploads/')
    fecha_subida = models.DateTimeField(auto_now_add=True)