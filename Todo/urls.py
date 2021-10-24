from django.urls import path
from . import views
app_name = 'todo'
urlpatterns = [
    path('', views.index, name='home'),
    path('edit_task/<str:pk>/', views.editTask, name='editTask'),
    path('delete_task/<str:pk>/', views.deleteTask, name='deleteTask'),

]