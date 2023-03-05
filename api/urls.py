from django.urls import path
from .views import todolist, singletodo

urlpatterns =[
   path('single/<int:id>/', singletodo),
    path('list/', todolist),
]