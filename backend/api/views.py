from django.views import View
from django.http.response import JsonResponse
from core.celery import app as celery_app

from .models import Book


class UploadFile(View):
    def post(self, request):
        if len(request.FILES) == 0:
            return JsonResponse({"message": "no files attached"})

        uploaded_file = request.FILES["file"]

        # 1. upload to aws s3

        # 2. send task to celery with aws s3 file path
        task = celery_app.send_task(
            "convert_audio_file_to_hls", args=[uploaded_file.name]
        )

        return JsonResponse(
            {
                "message": "File uploaded succesfully",
                "file": uploaded_file.name,
                "size": f"{round(uploaded_file.size / (1024 * 1024), 2)} mb",
                "type": uploaded_file.content_type,
            }
        )


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
        return JsonResponse({"test": "kjslfkd"})
