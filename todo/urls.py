from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_view, name='todo_view'),
    path('create/', views.create_view, name='create_view'),
    path('edit/<int:id>/', views.update_view, name='update_view'),
    path('delete/<int:id>/', views.delete_view, name='delete_view'),
]