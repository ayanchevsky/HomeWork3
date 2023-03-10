"""toodoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('current/', views.currenttodos, name='currenttodos'),
    path('all/', views.alltodos, name='alltodos'),
    path('complete/', views.completetodos, name='completetodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('todo/<int:todo_id>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_id>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_id>/continue', views.continuetodo, name='continuetodo'),
    path('todo/<int:todo_id>/delete', views.deletetodo, name='deletetodo'),

]
