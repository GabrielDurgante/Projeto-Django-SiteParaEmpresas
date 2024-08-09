from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres')
            return redirect('/usuarios/cadastro')
        
        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(request, constants.ERROR, 'Usuário ja existente')
            return redirect('/usuarios/cadastro')
        
        emails = User.objects.filter(email=email)

        if emails.exists():
            messages.add_message(request, constants.ERROR, 'Email ja cadastrado')
            return redirect('/usuarios/cadastro')
        
        
        user = User.objects.create_user(
            username=username,
            password=senha,
            email=email
        )

        return redirect('/usuarios/logar')