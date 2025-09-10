from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


Usuario = get_user_model()


def registrar_usuario(request):
    erro = None
    if request.method == "POST":
        apelido = request.POST.get("apelido")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        avatar = request.FILES.get("avatar")  # pega o arquivo
        bio = request.POST.get("bio")

        # 🔹 validações manuais
        if not username or not email or not password1:
            erro = "Preencha todos os campos."
        elif password1 != password2:
            erro = "As senhas não conferem."
        elif Usuario.objects.filter(username=username).exists():
            erro = "Esse nome de usuário já existe."
        else:
            # 🔹 cria o usuário
            user = Usuario.objects.create_user(
                username=username,
                email=email,
                password=make_password(password1),
                #password=password1,
                bio=bio,
            )

            if avatar:
                user.avatar = avatar
            
            user.save()

            login(request, user)
            return redirect("area_restrita")

    return render(request, "registro.html", {"erro": erro})


def login_usuario(request):
    erro = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("area_restrita")
        else:
            erro = "Usuário ou senha inválidos."

    return render(request, "login.html", {"erro": erro})


def logout_usuario(request):
    logout(request)
    return redirect("login")


@login_required
def area_restrita(request):
    return render(request, "area_restrita.html")
