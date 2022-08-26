from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import NewsViewSet


router1 = DefaultRouter()

router1.register("news", NewsViewSet, basename="news")
urlpatterns = [
    path("", include(router1.urls)),
]
