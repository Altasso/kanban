
from django.urls import path

from .views import kanban_board

urlpatterns = [
    path('', kanban_board, name='kanban_board')
]