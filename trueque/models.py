from django.db import models
from django.utils import timezone

class Post(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.fecha_publicacion = timezone.now()
		self.save()
	
	def __str__(self):
		return self.titulo

class Comment(models.Model):
	post = models.ForeignKey('trueque.Post', related_name='comments')
	autor = models.CharField(max_length=200)
	texto = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)
	aceptado = models.BooleanField(default=False)

	def approve(self):
		self.aceptado = True
		self.save()
	
	def __str__(self):
		return self.text
