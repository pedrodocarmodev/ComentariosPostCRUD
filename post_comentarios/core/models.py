from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(127)
    texto = models.TextField()
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now=True)