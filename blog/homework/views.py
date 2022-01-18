import logging
from django.http import HttpResponse
import pytest

from homework.models import User
from posts.models import Post

logger = logging.getLogger(__name__)


def show(obj):
    mass = []
    for obj_x in obj:
        mass.append(vars(obj_x))
    return mass



def homework_index_post(request):
    value = request.POST.get("email")
    value = request.POST.get("password")
    logger.info(value)
    return (value)


def homework_index(request):
    msg = request.GET.get("filter_posts_author")
    logger.info(msg)
    search_post = Post.objects.filter(author_id=msg)
    result = show(search_post)
    return HttpResponse(result)


    #Тренировка, поиск пользователя по емэйлу
"""    msg = request.GET.get("filter_email")
    search_person = User.objects.filter(email=msg).first()
    msg = request.GET.get("filter_email")
    logger.info(search_person)
    result=vars(search_person)
    print(result)"""

'''    msg = request.GET.get("name") or ""
    msg_1 = request.GET.get("error") or ""
    msg_2 = request.GET.get("repeat") or ""

    logger.info(msg)
    logger.info(msg_1)
    logger.info(msg_2)
    request = "7788"
    if msg_2 == "" and msg_1 == "":
        request = f"Добро пожаловать {msg}"
    if msg == "" and msg_2 == "":
        request = f"Ошибка {msg_1}"
    if msg == "" and msg_1 == "":
        request = f"Имя {msg_2} неккоректное."
        '''