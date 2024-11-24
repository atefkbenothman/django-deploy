from django.views import View
from django.http.response import JsonResponse
from .models import Book


class ListBooks(View):
    def get(self, request):
        books = Book.objects.all().values()
        return JsonResponse(list(books), safe=False)


class Ping(View):
    def get(self, request):
        return JsonResponse({"ping": "pong"})


class Health(View):
    def get(self, request):
        return JsonResponse({"health": "up"})


class Example(View):
    def get(self, request):
        return JsonResponse({"example": "example"})


class Test(View):
    def get(self, request):
        return JsonResponse({"test": "yup"})
