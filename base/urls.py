from  django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.home, name='home'),
    path('Addtask_form/', views.createTask, name='Add_task'),
    path('update_task/<int:pk>/', views.updateTask, name='update_task'),
    path('delete_task/<int:pk>/', views.deleteTask, name='delete_task'),
    path('task_Detail/<int:pk>/', views.taskDetail, name='task_Detail'),

]