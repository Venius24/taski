from django.test import TestCase
from rest_framework.test import APIClient

from .models import Task


class TaskApiTests(TestCase):
    def test_create_list_and_delete(self):
        client = APIClient()
        response = client.post('/api/tasks/', {'title': 'Read', 'description': 'Book'}, format='json')
        self.assertEqual(response.status_code, 201)
        task_id = response.data['id']
        self.assertEqual(str(Task.objects.get(pk=task_id)), 'Read')
        self.assertEqual(client.get('/api/tasks/').data[0]['id'], task_id)
        self.assertEqual(client.delete(f'/api/tasks/{task_id}/').status_code, 204)
        self.assertFalse(Task.objects.filter(pk=task_id).exists())
