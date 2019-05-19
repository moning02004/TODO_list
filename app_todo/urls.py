from django.urls import path

from . import views


app_name = 'app_todo'
urlpatterns = [
    path('continue/', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('new/', views.new, name='new'),
    path('complete/', views.complete_index, name='complete'),
    path('deadline/', views.deadline_index, name='dead'),

    path('_change/<int:pk>/', views.changePriority),
    path('_delete/<int:pk>/', views.delete, name='delete'),
    path('_finish/', views.finish),
]