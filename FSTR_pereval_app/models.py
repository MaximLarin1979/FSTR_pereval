from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    # модель для пользователей
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=254, default=None, verbose_name="Имя")
    second_name = models.CharField(max_length=254, default=None, verbose_name="Фамилия")
    surname = models.CharField(max_length=255, verbose_name="Отчество")
    email = models.EmailField(unique=True, default=None, verbose_name="Эл.почта")
    phone = models.CharField(max_length=64, verbose_name="Номер телефона")

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'

    class Meta:
        verbose_name_plural = "Пользователи"


class Coords(models.Model):
    # модель для координат перевала
    latitude = models.FloatField(max_length=254, verbose_name="Широта")
    longitude = models.FloatField(max_length=254, verbose_name="Долгота")
    height = models.IntegerField(verbose_name="Высота")

    def __str__(self):
        return f'Широта - {self.latitude}. Долгота - {self.longitude}. Высота - {self.height} метров.'

    class Meta:
        verbose_name_plural = "Координаты"


class PerevalAdded(models.Model):
    # модель для перевалов
    NEW, PENDING, ACCEPTED, REJECTED = 'N', 'P', 'A', 'R'
    STATUS_CHOICES = [(NEW, 'Новый'), (PENDING, 'Модерируется',), (ACCEPTED, 'Принят',), (REJECTED, 'Отклонен')]

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=NEW)
    beauty_title = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    other_titles = models.CharField(max_length=254)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")

    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='pereval')
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)

    level_spring = models.CharField(max_length=254, blank=True, verbose_name="Сложность весной")
    level_summer = models.CharField(max_length=254, blank=True, verbose_name="Сложность летом")
    level_autumn = models.CharField(max_length=254, blank=True, verbose_name="Сложность осенью")
    level_winter = models.CharField(max_length=254, blank=True, verbose_name="Сложность зимой")

    def __str__(self):
        return f"id: {self.pk}, title:{self.title}"

    class Meta:
        verbose_name_plural = "Данные перевалов"


class Images(models.Model):
    # модель для фотографий
    title = models.CharField(max_length=254, verbose_name="Название")
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_added = models.DateField(auto_now_add=True, verbose_name="Время добавления")

    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)

    def __str__(self):
        return f"id: {self.pk}, title:{self.title}"

    class Meta:
        verbose_name_plural = "Фотографии"
