from rest_framework import generics
from todo.models import TodoList
from .serializers import TodoSerializer

# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer