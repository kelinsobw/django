import logging
from django.http import HttpResponse
import pytest

logger = logging.getLogger(__name__)


def homework_index_post(request):
    value = request.POST.get("email")
    value = request.POST.get("password")
    logger.info(value)
    return HttpResponse()


def homework_index(request):
    print(request)
    msg = request.GET.get("name") or ""
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


    return HttpResponse(request)
