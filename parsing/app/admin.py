from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "pub_date", "tag_ext", "get_tags")
    search_fields = ("title", "pub_date", "tag_int")
    # list_filter = ("pub_date",)
    empty_value_display = "-пусто-"

    def get_tags(self, obj):
        return "\n".join([p.name for p in obj.tags.all()])
