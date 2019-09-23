from django.shortcuts import render, redirect
from .forms import LoginForm, SetPasswordForm
from django.contrib.auth.models import User

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Hatalı Giriş")
            return render(request, "login.html", context)

        messages.success(request, "Başarıyla Giriş Yapıldı")
        login(request, user)

        return redirect("index")

    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış Yapıldı")
    return redirect("index")


def changePassword(request):
    if request.user.is_authenticated:
        form = SetPasswordForm(request.POST or None)
        context = {
            "form": form,
            "username": request.user.username
        }
        if form.is_valid():
            user = request.user
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()

            messages.success(request, "Parola Başarıyla Değiştirildi")
            return redirect("user:login")
        return render(request, "changepassword.html", context)

    messages.warning(request, "Giriş Yapmadınız")
    return render(request, "index.html")


def register(request):
    form = SetPasswordForm(request.POST or None)
    user = User.objects.get(username="editör")
    print("User is ", user)
    print(type(user))

    if form.is_valid():
        password = form.cleaned_data.get("password")
        print(password)
        user.set_password(password)
        user.save()
        messages.success(request, "Parolanız Başarıyla Belirlenmiştir")
        return redirect("index")
    else:
        context = {
            "form": form
        }
        return render(request, "register.html", context)
