

import requests
import logging
import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from django.http import request
from rest_framework.authtoken.admin import User

from posts.models import Post

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Print posts"
    def handle(self, *args, **options):
        f = open(r'my_file_from_server.csv', "wb")
        posts_csv = requests.get("https://vk.com/doc441390880_624624602")
        f.write(posts_csv.content)
        with open(settings.BASE_DIR / "my_file_from_server.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                user, _ = User.objects.get_or_create(username=row[0])
                Post.objects.create(
                    author=user, title=row[1], slug=row[2], text=row[3]
                )

