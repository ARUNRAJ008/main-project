"""
URL configuration for front_end project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from fapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('admin_addAccount/', views.admin_addAccount),
    path('admin_database/', views.admin_database),
    path('admin_home/', views.admin_home),
    path('admin_event/', views.admin_event),
    path('admin_book/', views.admin_book),
    path('admin_db_client/', views.admin_db_client),
    path('admin_db_owner/', views.admin_db_owner),
    path('admin_db_tonment/', views.admin_db_tonment),
    path('login/', views.login),
    path('payment/', views.payment),
    path('profile_edit/', views.profile_edit),
    path('profile/', views.profile),
    path('profile_feedback/', views.profile_feedback),
    path('login/sigup/', views.sigup),
    path('slotBooking/', views.slotBooking),


]
