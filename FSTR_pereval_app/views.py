from django.http import JsonResponse
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
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
        # метод проверяет, можно ли редактировать данные, и реализует редактирование
        pk = kwargs.get("pk", None)
        try:
            instance = PerevalAdded.objects.get(pk=pk)
        except:
            return Response({"error": "Такого перевала не существует"}, status=400)
        if instance.status != "N":
            return Response({"message": "Перевал на модерации, данные изменить нельзя",
                             "state": 0}, status=400)
        else:
            serializer = PerevalDetailSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"state": 1}, status=200)


class AuthEmailPerevalAPI(mixins.ListModelMixin, viewsets.GenericViewSet):
    # класс для вывода данных по перевалам от пользователя по его адресу почты
    queryset = PerevalAdded.objects.all()
    serializer_class = AuthEmailPerevalSerializer

    def get(self, request, *args, **kwargs):
        # настройка метода get для возможности фильтрации и вывода записей по признаку адреса почты пользователя
        email = kwargs.get('email', None)
        if PerevalAdded.objects.filter(user__email=email).is_exist == True:
            responsedata = AuthEmailPerevalSerializer(PerevalAdded.objects.filter(user__email=email), many=True).data
        else:
            responsedata = {'message': f'Нет записей от пользователя с таким email = {email}'}
        return Response(responsedata, status=200)
