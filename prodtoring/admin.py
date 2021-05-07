from django.contrib import admin

from .models import Project, Person

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'status', "progress", "completedate"]

class PersonAdmin(admin.ModelAdmin):
    fields = ["name", "surname", "status", "telegram", "mail"]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Person, PersonAdmin)