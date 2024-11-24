from django.urls import path
from .views import Ping, Health, Example, Test, ListBooks

urlpatterns = [
    path("ping/", Ping.as_view(), name="ping"),
    path("health/", Health.as_view(), name="health"),
    path("example/", Example.as_view(), name="example"),
    path("test/", Test.as_view(), name="test"),
    path("books/", ListBooks.as_view(), name="list-books"),
]
