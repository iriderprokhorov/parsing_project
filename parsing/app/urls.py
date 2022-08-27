from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NewsBulkViewSet, NewsViewSet

router1 = DefaultRouter()

router1.register("news", NewsViewSet, basename="news")
router1.register("news_bulk", NewsBulkViewSet, basename="news_bulk")
urlpatterns = [
    path("", include(router1.urls)),
]
