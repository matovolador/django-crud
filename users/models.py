# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    edad = models.IntegerField()
    email = models.CharField(max_length=250)
    telefono = models.IntegerField()


    def create_user(self,params):
        User.objects.create(nombre=params['nombre'],apellido=params['apellido'],edad=params['edad'],email=params['email'],telefono=params['telefono']).save()
        return True

    def get_by_email(self,email):
        try:
            user = User.objects.filter(email=email).last()
            return user
        except User.DoesNotExist:
            return None

    def update_user(self,params):
        user = User.objects.get(id=params['id'])
        user.nombre = params['nombre']
        user.apellido = params['apellido']
        user.telefono = params['telefono']
        user.email = params['email']
        user.edad = params['edad']
        user.save()

    def is_num(self,var):
        try:
            int(var)
            return True
        except ValueError:
            return False
