from django.contrib import admin
from django.urls import path
from AcadeMeData import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    ]
