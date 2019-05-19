from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import MessageBox


def signin(request):
    message = None
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST.get('username'))
            if user.check_password(request.POST.get('password')):
                auth.login(request, user)
                return redirect('app_main:index')
            else:
                message = '해당 계정을 찾을 수 없습니다.'
        except:
            message = '해당 계정을 찾을 수 없습니다.'
    return render(request, 'app_user/signin.html', {'message': message})


def signup(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('firstName')
        user.last_name = request.POST.get('lastName')
        user.set_password(request.POST.get('password'))
        user.save()
        MessageBox(user=user).save()
        return redirect('app_user:signin')


def message(request):
    message_list = request.user.messagebox.message_set.all().order_by('id').reverse()
    request.user.messagebox.unread = 0
    request.user.messagebox.save()
    return render(request, 'app_user/message.html', {'message_list': message_list})


def signout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('app_main:index')


def check(request):
    message = 'good' if not User.objects.all().filter(username=request.GET.get('username')).exists() else 'bad'
    return JsonResponse({'message': message})

