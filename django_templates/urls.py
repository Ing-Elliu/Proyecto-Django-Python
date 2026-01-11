"""
URL configuration for django_templates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('juego/hokai_star_rail/',views.hokai_star_rail,name='hokai_star_rail'),
    path('juego/genshin_impact/',views.genshin_impact,name='genshin_impact'),
    path('juego/wutering_waves/',views.wutering_waves,name='wutering_waves'),

    path('supabase/',include('app_supabase.urls')),
    path('personajes/',include('app_personajes.urls')),
    path('blog/',include('app_blog.urls'))
]
