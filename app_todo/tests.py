from django.test import TestCase, Client

from app_todo.models import Todo
from app_user.models import User


class TodoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user(username='user1', password='password1', name='user_1')
        User.objects.create_user(username='user2', password='password2', name='user_2')
        Todo.objects.create(author=user1, title='todo_1', content="todo_1's content")
        Todo.objects.create(author=User.objects.get(pk=1), title='todo_2', content="todo_2's content")

    def test_create(self):
        client = Client()
        client.login(username='user1', password='password1')
        client.post('/todo/new', {'title': 'todo_3', 'content': "todo_3's content"})
        todo = Todo.objects.get(pk=3)
        self.assertIsNotNone(todo)

    def test_delete(self):
        client = Client()
        client.login(username='user1', password='password1')

        before = len(Todo.objects.all())
        todo = Todo.objects.get(pk=1)
        response = client.post(f'/todo/{todo.id}/delete')
        after = len(Todo.objects.all())
        self.assertNotEqual(before, after)

    def test_delete_not_owner(self):
        client = Client()
        client.login(username='user2', password='password2')

        before = len(Todo.objects.all())
        todo = Todo.objects.get(pk=1)
        response = client.post(f'/todo/{todo.id}/delete')
        after = len(Todo.objects.all())
        self.assertEqual(before, after)

    def test_update(self):
        client = Client()
        client.login(username='user1', password='password1')

        todo = Todo.objects.get(pk=2)
        response = client.post(f'/todo/{todo.id}/edit', {'title': 'todo_new_2', 'content': todo.content})
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'todo_new_2')

