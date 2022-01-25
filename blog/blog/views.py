import logging

from django.conf.global_settings import AUTH_USER_MODEL
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from blog.forms import RegisterForm, PostsForm
from posts.models import Post

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process validated data
            logger.info(form.cleaned_data)
            user = User(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def posts(request):
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            # Process validated data
            logger.info(form.cleaned_data)
            post = Post(
                author_id=1,
                title=form.cleaned_data['title'],
                image=form.cleaned_data['image'],
                slug=form.cleaned_data['slug'],
                text=form.cleaned_data['text']
            )
            post.save()
            return redirect("/")
    else:
        form = PostsForm()
    return render(request, "posts.html", {"form": form})
