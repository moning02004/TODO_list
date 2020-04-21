from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from app_user import views

app_name = 'app_user'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('signup/', views.UserRegisterView.as_view(), name='signup'),
    path('<int:pk>/notice/', views.message, name='message'),

    path('logout/', LogoutView.as_view(next_page=reverse_lazy('app_main:index')), name='logout'),
    path('_check/', views.check),
]
