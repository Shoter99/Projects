from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('<name>', views.name, name='User name')
        ]
