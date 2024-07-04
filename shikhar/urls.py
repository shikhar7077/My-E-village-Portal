"""Project1 URL Configuration

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
from shikhar import views

urlpatterns = [
    path('admin/', admin.site.urls),#super_user_login(devloper)
    path('',views.home, name='home'),
    path('AboutVillage/',views.aboutvillage,name='aboutvillage'),
    path('devlopmentintiative/',views.devlopmentintiative,name='devlopmentintiative'),
    path('schools/',views.schools,name='schools'),
    path('S_activities/',views.S_activities,name='S_activities'),
    path('S_achivments/',views.S_achivments,name='S_achivments'),
    path('gram_panchayat/',views.gram_panchayat,name='gram_panchayat'),
    path('body/',views.body,name='body'),
    path('updates/',views.updates,name='updates'),
    path('achivements/',views.achivements,name='achivements'),
    path('donation/',views.donation,name='donation'),
    path('Collaboration/',views.Collaboration,name='Collaboration'),
    path('login/',views.user_login,name='login'),
    
   
]
