from .models import Users, Coords, PerevalAdded
from rest_framework import serializers


class PerevalAddedSerializer(serializers.ModelSerializer):
    # класс сериализатора для перевала
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    coords = serializers.PrimaryKeyRelatedField(queryset=Coords.objects.all())

    class Meta:
        model = PerevalAdded
        # параметр depth необходим для раскрытия информации по вложенным объектам
        depth = 1
        fields = ("beauty_title",
                  "title",
                  "other_titles",
                  "connect",
                  "add_time",
                  "user",
                  "coords",
                  "level_winter",
                  "level_summer",
                  "level_autumn",
                  "level_spring",
                  )
