from django.contrib import admin

from .models import Project, Person, Task

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    fields = ["title", "status", "progress", "completedate", "description", "pic_url"]


class PersonAdmin(admin.ModelAdmin):
    fields = ["name", "surname", "status", "telegram", "mail", "skills", "project", "pic_url"]


class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Информация о задаче', {'fields': ['title', "weight", "description"]}),
        ('Информация о проекте', {'fields': ['project']}),
        ("Информация о работяге", {"fields": ["responsible"]})
    ]
    list_filter = ["project"]
    list_display = ('title', 'deadline', 'weight', "responsible")
    
    class Meta:
        ordering = ['weight',]
        # fields = ["project", "title", "weight", "description", "responsible"]


admin.site.register(Project, ProjectAdmin)

admin.site.register(Task, TaskAdmin)

admin.site.register(Person, PersonAdmin)

