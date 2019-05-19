from django.urls import path

from app_user import views

app_name = 'app_user'
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('message/', views.message, name='message'),

    path('_signout/', views.signout, name='signout'),
    path('_check/', views.check),
]