from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('board', views.board, name="board"),
    path('board_write', views.board_write, name="board_write"),
    path('board_insert', views.board_insert, name="board_insert"),
]