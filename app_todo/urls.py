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
    path('<int:pk>/complete/', views.complete_index, name='complete'),

    path('continue/edit/', views.index_edit, name='index_edit'),
    path('deadline/', views.deadline_index, name='dead'),

    path('_change/<int:pk>/', views.changePriority),
    path('_delete/<int:pk>/', views.delete, name='delete'),
    path('_finish/', views.finish),
]
