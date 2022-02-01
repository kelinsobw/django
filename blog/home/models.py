from django.conf import settings
from django.db import models


class Home(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="home"    )
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    floor = models.IntegerField()
    floors = models.IntegerField()
    price = models.FloatField()
    square = models.FloatField()
    tel = models.CharField(max_length=20)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
