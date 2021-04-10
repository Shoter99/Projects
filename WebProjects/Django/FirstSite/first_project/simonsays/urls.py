from django.urls import path
from . import views

urlpatterns = [
        path('log/', views.login, name='login'),
        path('game/<name>', views.index, name="game"),
        ]
