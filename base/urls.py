from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_user, name='login'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name='register'),
    path('update-user/', views.update_user, name='update-user'),
    path('home/', views.home, name='home'),
    path('create-task/', views.create_task, name='create-task'),
    path('task/<str:pk>/', views.task, name='task'),
    path('update-task/<str:pk>/', views.update_task, name='update-task'),
    path('delete-task/<str:pk>/', views.delete_task, name='delete-task'),
]
