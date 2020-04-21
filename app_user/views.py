from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserCreateForm
from .models import User


class UserLoginView(LoginView):
    template_name = 'app_user/auth.html'
    extra_context = {'auth': 'login'}

    def form_invalid(self, form):
        form.error_messages['message'] = '해당 사용자를 찾을 수 없습니다.'
        return super().form_invalid(form)


class UserRegisterView(CreateView):
    template_name = 'app_user/auth.html'
    success_url = reverse_lazy('app_user:login')
    form_class = UserCreateForm
    extra_context = {'auth': 'signup'}


def message(request):
    message_list = request.user.messagebox.message_set.all().order_by('id').reverse()
    request.user.messagebox.unread = 0
    request.user.messagebox.save()
    return render(request, 'app_user/message.html', {'message_list': message_list})


def check(request):
    message = 'good' if not User.objects.all().filter(username=request.GET.get('username')).exists() else 'bad'
    return JsonResponse({'message': message})
