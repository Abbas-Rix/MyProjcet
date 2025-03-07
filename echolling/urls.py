"""
URL configuration for echolling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
from django.urls import include, path
from . import views
from django.contrib import admin 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index-two', views.index2),
    path('index-three', views.index3),
    path('index-four', views.index4),
    path('index-five', views.index5),
    path('index-six', views.index6),
    path('index-seven', views.index7),
    path('about', views.about),
    path('blog-details', views.blog_details),
    path('blog', views.blog),
    path('contact', views.contact),
    path('coureses-grid', views.coureses_grid),
    path('coureses-list', views.coureses_list),
    path('coureses-right-sidebar', views.coureses_right_sidebar),
    path('coureses-single', views.coureses_single),
    path('events-right-sidebar', views.events_right_sidebar),
    path('events-single', views.events_single),
    path('events', views.events),
    path('instructors', views.instructors),
    path('login', views.login),
    path('profile', views.profile),
    path('signup', views.signup),

]
