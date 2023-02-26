from rest_framework import serializers
from todo.models import TodoList

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('title', 'content', 'date_created',)