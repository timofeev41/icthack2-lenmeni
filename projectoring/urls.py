from django.contrib import admin
from django.urls import path, include

from prodtoring.views import view_homepage, view_project_homepage, view_user_list, view_current_user

urlpatterns = [
    path('', view_homepage, name='index'),
    path('project=<int:project_id>/', view_project_homepage, name="Project page by ID"),
    path('users/', view_user_list, name="Get all users"),
    path('user=<int:user_id>/', view_current_user, name="Get user by ID" ),

    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
    # path('login/', /)
]
