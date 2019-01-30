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
        user = authenticate(request, username=username, password=password)  # Faz a autenticação do usuário
        if (user is not None) and (user.is_active):  # Se existir usuário cadastrado e ele for ativo
            auth_login(request, user)  # Faz o login do usuário
            return redirect('sala')
        else:
            contexto = {'flag': False, 'msg': 'Email e Senha não correspondem', 'username': username, 'password': password}
            return render(request, "core/login.html", contexto)


def sala(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            user = request.user
            auth_logout(request)
            ctx = {'firstName': user.first_name, 'lastName': user.last_name, 'username': user.username}
            isTx = user.groups.filter(name='TX').exists()
            isRx = user.groups.filter(name='RX').exists()
            if isTx == isRx and isTx is not False:
                return render(request, "core/login.html", {'flag': False, 'msg': 'Usuário com mais de um grupo', 'username': user.username, 'password': ""})

            if isTx:
                try:
                    ctx['rom'] = Sala.objects.filter(userTx=user.id)[0]
                    return render(request, 'sala/tx.html', ctx)
                except IndexError:
                    return render(request, "core/login.html", {'flag': False, 'msg': 'Esse usuário não tem sala definida', 'username': user.username, 'password': ""})
            elif isRx:
                try:
                    ctx['rom'] = Sala.objects.filter(userRx=user.id)[0]
                    return render(request, 'sala/rx.html', ctx)
                except IndexError:
                    return render(request, "core/login.html", {'flag': False, 'msg': 'Esse usuário não tem sala definida', 'username': user.username,  'password': ""})

            else:
                return render(request, "core/login.html", {'flag': False, 'msg': 'Você não tem grupo definido', 'username': user.username, 'password': ""})

        else:
            auth_logout(request)
            return redirect('login')
    else:
        return redirect('login')
