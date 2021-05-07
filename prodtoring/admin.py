from django.contrib import admin

from .models import Tasks

# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    fields = ['title', 'status', "progress", "completedate"]

admin.site.register(Tasks, TasksAdmin)