from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader, context

from .models import Project, Person

# Create your views here.
def view_homepage(request):
    projects = Project.objects.all()
    template = loader.get_template('index.html')
    context = {
        'projects': projects
    }
    return HttpResponse(template.render(context, request))


def view_project_homepage(request, project_id):
    project = Project.objects.all().filter(id=project_id)
    template = loader.get_template('project.html')
    context = {
        "project": project
    }
    return HttpResponse(template.render(context, request))

def view_user_list(request):
    users = Person.objects.all()
    template = loader.get_template('persons.html')
    context = {
        "users": users
    }
    return HttpResponse(template.render(context, request))