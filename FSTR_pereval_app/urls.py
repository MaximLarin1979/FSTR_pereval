from django.urls import path
from .views import PerevalAddedAPI

urlpatterns = [
    path('submitData', PerevalAddedAPI.as_view()),
    ]
