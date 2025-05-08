from django.shortcuts import render
from .models import Board_Column
# Create your views here.

def kanban_board(request):
    columns = Board_Column.objects.prefetch_related('task_set').order_by('position')
    return render(request, 'tasks/kanban_board.html', {'columns': columns})