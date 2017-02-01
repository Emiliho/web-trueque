from django.db import models
from django.contrib.auth.models import User

class Circunscripcion(models.Model):
	nombre = models.CharField(max_length=50)
	escanos = models.IntegerField('escaños', default=0)

	def __str__(self):
		return self.nombre

class Mesa(models.Model):
	nombre = models.CharField(max_length=50)
	circunscripcion = models.ForeignKey(Circunscripcion, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Partido(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	
	def __str__(self):
		return self.nombre

class Resultado(models.Model):
	partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
	mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
	votos = models.IntegerField(default=0)

	def __str__(self):
		return self.partido.nombre + ' ' + self.mesa.nombre


class Usuario(models.Model):
	usuario = models.OneToOneField(User, unique=True)
	usuario_gestor='GES'
	usuario_supervisor='SUP'
	tipos=((usuario_gestor, 'Usuario gestor'),(usuario_supervisor, 'Usuario supervisor'))
	tipo = models.CharField(max_length=3, choices=tipos)
	
	def __str__(self):
		return self.usuario.username + ' Tipo usuario: ' + self.tipo 	
