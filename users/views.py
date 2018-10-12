# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
# Create your views here.


def list(request):
    users = User.objects.order_by('id')
    return render(request, 'users/list.html',{'users':users})


def edit(request,user_id):
    if request.method == 'POST':
        users = User()

        nombre = request.POST.get('nombre',False)
        apellido = request.POST.get('apellido',False)
        email = request.POST.get('email',False)
        telefono = request.POST.get('telefono',False)
        edad = request.POST.get('edad',False)


        ## VALIDATION
        if (edad) and (users.is_num(edad)==False):
            return HttpResponse("Error: Edad debe ser un número entero")

        if (telefono) and (users.is_num(telefono)==False):
            return HttpResponse("Error: Teléfono debe ser un número entero")

        if (email):
            try:
                validate_email(email)
            except ValidationError as e:
                return HttpResponse("Error: El email no tiene un formato correecto")
        if nombre == False or apellido == False or email == False or telefono == False or edad == False:
            return HttpResponse("Error: Uno de los campos está vacío.")

        user_by_email = users.get_by_email(email)
        print(type(user_by_email.id))
        print(type(user_id))
        if user_by_email is not None and user_by_email.id != int(user_id):
            return HttpResponse("Error: Ese email ya está en uso.")
        ## END VALIDATION

        user = users.update_user({"id":user_id,"nombre":nombre,"apellido":apellido,"email":email,"telefono":telefono,"edad":edad})
        return HttpResponse("Usuario editado con éxito!")

    else:
        user = get_object_or_404(User,id=user_id)
        return render(request, 'users/edit.html',{'user':user})


def delete(request,user_id):
    res = User.objects.filter(id=user_id).delete()
    print(res[0])
    if (res[0]==0):
        return HttpResponse("No se ha encontrado un usuario con esa id.")
    return HttpResponse("Usuario eliminado")


def create(request):
    users = User()
    if request.method == 'POST':

        nombre = request.POST.get('nombre',False)
        apellido = request.POST.get('apellido',False)
        email = request.POST.get('email',False)
        telefono = request.POST.get('telefono',False)
        edad = request.POST.get('edad',False)


        ## VALIDATION
        if (edad) and (users.is_num(edad)==False):
            return HttpResponse("Error: Edad debe ser un número entero")

        if (telefono) and (users.is_num(telefono)==False):
            return HttpResponse("Error: Teléfono debe ser un número entero")

        if (email):
            try:
                validate_email(email)
            except ValidationError as e:
                return HttpResponse("Error: El email no tiene un formato correecto")
        if nombre == False or apellido == False or email == False or telefono == False or edad == False:
            return HttpResponse("Error: Uno de los campos está vacío.")

        user_by_email = users.get_by_email(email)
        if user_by_email is not None:
            return HttpResponse("Error: Ese email ya está en uso.")

        ## END VALIDATION

        flag = users.create_user({"nombre":nombre,"apellido":apellido,"email":email,"telefono":telefono,"edad":edad})

        return HttpResponse("Usuario creado!")

    else:
        return render(request, 'users/create.html')
