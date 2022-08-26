from django.contrib import admin
from .models import News, Tag


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "pub_date", "tag_ext")
    search_fields = ("title", "pub_date", "tag_int")
    # list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "news")
