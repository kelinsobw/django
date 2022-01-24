# views.py
from django.shortcuts import render

from blog.forms import RegisterForm


def register(request):
    form = RegisterForm()
    return render(request, "register.html", {"form": form})
