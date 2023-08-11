from rest_framework import serializers
from tasks.models import Task

from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Task
        fields = ["id", "title", "text", "state", "author", "priority"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name="task-detail", read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "tasks"]