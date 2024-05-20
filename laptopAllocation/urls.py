"""
URL configuration for laptopAllocation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from laptopAllocation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.INDEX,name="home"),
    path('laptop/',views.LAPTOP,name="laptop"),
    path('laptop/create/',views.LAPTOP_CREATE,name="laptop_create"),
    path('laptop/update/<str:id>',views.LAPTOP_UPDATE,name="laptop_update"),
    path('laptop/delete/<str:id>',views.LAPTOP_DELETE,name="laptop_delete"),

    path('batch/',views.BATCH,name="batch"),
    path('batch/create/',views.BATCH_CREATE,name="batch_create"),
    path('batch/update/<str:id>',views.BATCH_UPDATE,name="batch_update"),
    path('batch/delete/<str:id>',views.BATCH_DELETE,name="batch_delete"),

    path('student/',views.STUDENT,name="student"),
    path('student/create/',views.STUDENT_CREATE,name="student_create"),
    path('student/update/<str:id>',views.STUDENT_UPDATE,name="student_update"),
    path('student/delete/<str:id>',views.STUDENT_DELETE,name="student_delete"),

    path('allocation/',views.ALLOCATION,name="allocation")
]
