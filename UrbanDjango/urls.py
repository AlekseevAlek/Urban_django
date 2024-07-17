from django.contrib import admin
from django.urls import path, include
from task2 import views # Подставьте ваш модуль и предполагаемую функцию или класс вместо views
print("UrbanDjango.urls loaded")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task2'))

 ]
