from django.contrib import admin
from django.urls import path
from AcadeMe import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,  name='homepage')
    ]
