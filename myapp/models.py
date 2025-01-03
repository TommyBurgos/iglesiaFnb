from django.db import models

# Create your models here.
class BlogNoticia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='blog_images/', default='blog1.jpg')
    titulo = models.CharField(max_length=200)
    noticia = models.CharField(max_length=100000)

class CarruselPrincipal(models.Model):
    img1 = models.ImageField(upload_to='carrusel/', default='carrusel/default.jpg')
    titulo1 = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)    

    def __str__(self):
        return f"Imagen: {self.img1} -- Titulo: {self.titulo1}"