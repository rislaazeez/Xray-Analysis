"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_settings', views.admin_settings, name='admin_settings'),
    path('admin_settings_404', views.admin_settings_404, name='admin_settings_404'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),

    path('admin_category_master_add', views.admin_category_master_add, name='admin_category_master_add'),
    path('admin_category_master_view', views.admin_category_master_view, name='admin_category_master_view'),
    path('admin_category_master_delete', views.admin_category_master_delete, name='admin_category_master_delete'),

    path('admin_staff_master_add', views.admin_staff_master_add, name='admin_staff_master_add'),
    path('admin_staff_master_view', views.admin_staff_master_view, name='admin_staff_master_view'),
    path('admin_staff_master_delete', views.admin_staff_master_delete, name='admin_staff_master_delete'),

    path('admin_pic_pool_add', views.admin_pic_pool_add, name='admin_pic_pool_add'),
    path('admin_pic_pool_view', views.admin_pic_pool_view, name='admin_pic_pool_view'),
    path('admin_pic_pool_delete', views.admin_pic_pool_delete, name='admin_pic_pool_delete'),
    path('admin_user_test_master_view', views.admin_user_test_master_view, name='admin_user_test_master_view'),

    path('staff_login', views.staff_login_check, name='staff_login'),
    path('staff_home', views.staff_home, name='staff_home'),
    path('staff_user_test_master_add', views.staff_user_test_master_add, name='staff_user_test_master_add'),
    path('staff_user_test_master_view', views.staff_user_test_master_view, name='staff_user_test_master_view'),
    path('staff_settings', views.staff_settings, name='staff_settings'),
    path('staff_changepassword', views.staff_changepassword, name='staff_changepassword'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_home', views.user_home, name='user_home'),
    path('user_test_master_view', views.user_test_master_view, name='user_test_master_view'),
    path('user_settings', views.user_settings, name='user_settings'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),
]
