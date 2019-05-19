from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('app_todo:index')
    return render(request, 'app_user/signup.html')