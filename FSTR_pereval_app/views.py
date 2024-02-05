from django.http import JsonResponse
from rest_framework import generics, viewsets, mixins
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


class PerevalDetailAPI(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    # класс для получения детальных данных по перевалу и для редактирования этих данных (если status=NEW)
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalDetailSerializer

    def update(self, request, *args, **kwargs):
        """
        Переопределение метода update(PATCH)
        """
        pk = kwargs.get("pk", None)

        try:
            instance = PerevalAdd.objects.get(pk=pk)
        except:
            return Response({"error": "Такого перевала не существует"}, status=400)

        if instance.status != "N":
            return Response({"message": "Перевал на модерации, вы не можете его изменить",
                             "state": 0}, status=400)
        else:
            serializer = PerevalDetailSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"state": 1}, status=200)
