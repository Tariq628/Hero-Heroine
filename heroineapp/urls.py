from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('renewal/', views.renewal, name='renewal'),
    path('signup/', views.sign_up, name='sign_up'),
    path('profile/', views.profile),
    path('sub-user/', views.sub_user, name='sub_user'),
    path('user-info/', views.user_info, name='user_info'),
    path('login/', views.user_login),
    path('logout/', views.user_logout, name='logout'),
    path('select-profile/', views.select_profile),
    path('brands/', views.brands, name='brands'),
    path('categories/<int:brand_id>/', views.category, name='categories'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('user-profile-edit/', views.user_profile_edit),

    path('user-edit/<int:id>/', views.user_edit, name='user_edit'),
    path('subuser-edit/<int:id>/', views.subuser_edit, name='subuser_edit'),
    path('user-delete/<int:id>/', views.user_delete, name='user_delete'),
    path('subuser-delete/<int:id>/', views.subuser_delete, name='subuser_delete'),
]
