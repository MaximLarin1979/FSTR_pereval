from django.http import JsonResponse
from rest_framework import generics
from .serializers import *


class PerevalAddedAPI(generics.CreateAPIView):
    # класс для работы с БД, в нем настраиваем метод post - отправка данных о перевале
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def post(self, request):
        # настройка метода post
        pereval = PerevalAddedSerializer(data=request.data)
        try:
            if pereval.is_valid(raise_exception=True):
                pereval.save()
                data = {'status': '200', 'message': 'null', 'id': f'{pereval.instance.id}'}
                return JsonResponse(data, status=200, safe=False)

        except Exception as exc:
            responsedata = {'status': '400', 'message': f'Bad Request: {exc}', 'id': 'null'}
            return JsonResponse(responsedata, status=400, safe=False)
