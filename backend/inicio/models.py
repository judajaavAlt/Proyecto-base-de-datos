from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuarios_id = models.CharField(max_length=100, primary_key=True)
    apellidos_usuario = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=200)
    correo_electronico = models.CharField(max_length=100)
    foto_perfil = models.CharField(max_length=100)
    telefono = models.CharField(max_length=13)
    direccion = models.CharField(max_length=100)

class Trabajador(models.Model):
    trabajador_id = models.CharField(max_length=100, unique=True)
    usuarios_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    foto_id = models.CharField(max_length=100)
    calificacion = models.IntegerField()

class Labor(models.Model):
    labor_id = models.CharField(max_length=100, primary_key=True)
    nombre_labor = models.CharField(max_length=100)
    disponibilidad = models.CharField(max_length=2)

class TrabajadorLabor(models.Model):
    labor_id = models.ForeignKey(Labor, on_delete=models.CASCADE)
    trabajador_id = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    precio = models.IntegerField()

class Cliente(models.Model):
    cliente_id = models.CharField(max_length=100, primary_key=True)
    usuarios_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    medio_pago = models.CharField(max_length=100)
    foto_recibo = models.CharField(max_length=100)

class ClienteLabor(models.Model):
    labor_id = models.ForeignKey(Labor, on_delete=models.CASCADE)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pago = models.IntegerField()
    calificacion = models.IntegerField()