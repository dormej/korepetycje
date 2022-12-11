"""project URL Configuration

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
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_nested_admin/', include('nested_admin.urls')),
    path('auth/', include('rest_authtoken.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('teachers/', views.teacher_list),
    path('teachers/<int:pk>/', views.teacher_detail),
    path('teachers/update/<int:pk>/', views.teacher_update),
    path('teachers/delete/<int:pk>/', views.teacher_update_delete),
    path('students/', views.student_list),
    path('groups/<int:pk>/', views.group_detail),
    path('groups/', views.group_list),
    path('groups/<int:pk>/participants', views.group_participants),
    path('students-of/<int:pk>/teacher', views.teacher_students),
]
