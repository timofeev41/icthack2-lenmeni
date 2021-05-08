from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegisterFormView.as_view(), name="register"),
]
