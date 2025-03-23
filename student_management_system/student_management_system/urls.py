"""
URL configuration for student_management_system project.

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
from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_views,Staff_Views,Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('Hod/Home',Hod_views.HOME,name='hod_home'),
    path('Hod/Student/Add',Hod_views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>', Hod_views.EDIT_STUDENT, name='edit_student'),
    path('doLogout',views.doLogout,name='doLogout'),

    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
