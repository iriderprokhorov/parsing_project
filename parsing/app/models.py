from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    """Модель тегов"""

    name = models.CharField("Тег", max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    """Модель новостей."""

    title = models.TextField("Название")
    pub_date = models.DateField("Дата публикации")
    tag_ext = models.CharField("Тег внешний", max_length=200)
    tag_int = models.ManyToManyField(Tag, through="TagNews")

    def __str__(self):
        return self.title


class TagNews(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tag} {self.news}"