from django.contrib import admin
from django.urls import path
from base.views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',Tasklist.as_view(),name='TaskList'),
    path('register/',registerPage.as_view(),name='register'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreation.as_view(),name='task-create'),
    path('update-task/<int:pk>/',TaskUpdtat.as_view(),name='task-update'),
    path('delete-task/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',Logoutview.as_view(next_page='TaskList'),name='logout')
    ] 