from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

# Create your views here.


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Giriş başarılı!")
            return redirect("index")  # giriş sonrası yönlendirme
        else:
            messages.error(request, "Geçersiz e-posta ya da şifre.")

    return render(request, "account/login.html")


def register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Şifreler uyuşmuyor.")
            return render(request, "account/register.html")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Bu e-posta ile kayıtlı bir kullanıcı zaten var.")
            return render(request, "account/register.html")

        user = User.objects.create_user(username=email, email=email, password=password1)
        user.first_name = fullname.split()[0]
        user.last_name = (
            " ".join(fullname.split()[1:]) if len(fullname.split()) > 1 else ""
        )
        user.save()

        auth_login(request, user)  # <-- Hatalı 'login()' yerine bu
        messages.success(request, "Başarıyla kayıt oldunuz ve giriş yaptınız.")
        return redirect("index")

    return render(request, "account/register.html")


def logout_view(request):
    auth_logout(request)
    return redirect("login")
