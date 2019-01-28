from django.urls import path
from .views import login, sala


urlpatterns = [
    path('', login, name='login'),
    path('sala', sala, name='sala'),
]