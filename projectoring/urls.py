from django.contrib import admin
from django.urls import path

from prodtoring.views import view_homepage, view_project_homepage, view_user_list

urlpatterns = [
    path('', view_homepage, name='index'),
    path('project=<int:project_id>/', view_project_homepage, name="project page"),
    path('admin/', admin.site.urls),
    path('users/', view_user_list),
]
