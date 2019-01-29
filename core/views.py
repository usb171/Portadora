from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from core.models import Sala

def login(request):

    if request.method == 'GET':
        auth_logout(request)
        return render(request, 'core/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # Faz a autenticação do usuário
        if (user is not None) and (user.is_active): # Se existir usuário cadastrado e ele for ativo
            auth_login(request, user) # Faz o login do usuário
            return redirect('sala')
        else:
            contexto = {'flag': False, 'msg': 'Email e Senha não correspondem', 'username': username, 'password': password}
            return render(request, "core/login.html", contexto)


def sala(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            if request.user.groups.filter(name='TX').exists():
                sala = Sala.objects.filter(userTx=request.user.id)[0]
                contexto = {"salaId": sala.hash, "nomeSala": sala.nomeSala, 'usuario': request.user.username}
                auth_logout(request)
                return render(request, 'sala/tx.html', contexto)
            elif request.user.groups.filter(name='RX').exists():
                sala = Sala.objects.filter(userRx=request.user.id)[0]
                contexto = {"salaId": sala.hash, "nomeSala": sala.nomeSala, 'usuario': request.user.username}
                auth_logout(request)
                return render(request, 'sala/rx.html', contexto)
            else:
                auth_logout(request)
                contexto = {'flag': False, 'msg': 'Você não tem grupo definido', 'username': request.user.username, 'password': ""}
                return render(request, "core/login.html", contexto)
        else:
            auth_logout(request)
            return redirect('login')

    else:
        return redirect('login')

