from django.shortcuts import render, redirect

from .forms import RegisterForm

def welcome(response):
    return render(response, 'register/welcome.html')

def register(response):
    err = ""

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            err = form.errors


    form = RegisterForm()
    return render(response, "register/register.html", {"form": form, "error": err})

