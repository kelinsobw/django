from django.contrib import admin
from home.models import Home


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "floor", "floors", "price", "square", "created_at", "tel")
    fields = ("author", "title", "floor", "floors", "price", "square", "created_at", "tel")
    readonly_fields = ("created_at",)
    search_fields = ("title", "floor", "square")

