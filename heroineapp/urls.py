from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('renewal/', views.renewal, name='renewal'),
    path('register/', views.register),
    path('sub-user/', views.sub_user),
    path('user-info/', views.user_info),
    path('login/', views.user_login),
    path('logout/', views.user_logout, name='logout'),
    path('select-profile/', views.select_profile),
    path('brands/', views.brands),
    path('categories/<int:brand_id>/', views.category, name='categories'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('user-profile-edit/', views.user_profile_edit),
]
