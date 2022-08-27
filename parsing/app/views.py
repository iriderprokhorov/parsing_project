from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("pub_date", "tag_ext")
    search_fields = ("tags__name", "^pub_date", "tag_ext", "title")


class CreateListMixin:
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)


class NewsBulkViewSet(CreateListMixin, viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
