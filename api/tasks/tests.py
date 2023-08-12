from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient, APIRequestFactory

from .views import TaskViewSet


class NewTaskCreatingTest(TestCase):
    def setUp(self):
        User.objects.create_superuser(username="test", email="test@gmail.com", password="simple_password_1234567890")
        api_client = APIClient()
        api_client.login(username="test", password="simple_password_1234567890")

        api_client.post("/tasks/", {"title": "Task 1", "text": "Text of task 1.", "state": "in_process", "priority": "medium"}, format="json")
        api_client.post("/tasks/", {"title": "Task 2", "text": "Text of task 2.", "state": "accepted", "priority": "high"}, format="json")

        api_client.logout()
    
    def test_newly_created_tasks(self):
        task_view_set = TaskViewSet.as_view({"get": "retrieve"})
        api_request_factory = APIRequestFactory()

        request = api_request_factory.get("/tasks/")
        
        response = task_view_set(request, pk=1)
        self.assertEqual(response.status_code, 200)

        response = task_view_set(request, pk=2)
        self.assertEqual(response.status_code, 200)