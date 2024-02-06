from django.urls import path
from .views import PerevalAddedAPI, PerevalDetailAPI, AuthEmailPerevalAPI

urlpatterns = [
    path('submitData', PerevalAddedAPI.as_view()),
    path('submitData/<int:pk>/', PerevalDetailAPI.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
    path('submitData/user__email=<str:email>', AuthEmailPerevalAPI.as_view({'get': 'list'})),
    ]
