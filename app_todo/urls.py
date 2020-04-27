from django.urls import path

from . import views
from .views import *

app_name = 'app_todo'
urlpatterns = [
    path('', TodoListView.as_view(), name='index'),
    path('new', TodoCreateView.as_view(), name='new'),
    path('<int:pk>', TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', TodoUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', TodoDeleteView.as_view(), name='delete'),
]
