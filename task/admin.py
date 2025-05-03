from django.contrib import admin
from .models import Task, Board_Column
# Register your models here.
@admin.register(Board_Column)
class Board_Column_Admin(admin.ModelAdmin):
    list_display = ('name', 'position')
    ordering = ('position',)

@admin.register(Task)
class Task_Admin(admin.ModelAdmin):
    list_display = ('title', 'assignee', 'status', 'priority', 'due_date', 'created_at')
    list_filter = ('status', 'priority', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('due_date',)