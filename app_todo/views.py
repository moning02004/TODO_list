from django.http import JsonResponse
from django.shortcuts import render, redirect

from app_user.models import MessageBox, Message
from .models import Todo
import datetime


def index(request):
    todo_list = request.user.todo_set.all().filter(isFinish='no')
    today = datetime.datetime.now().strftime('%Y.%m.%d')
    for todo in [x for x in todo_list if x.deadline is not None and x.deadline.strftime('%Y.%m.%d') < today]:
        if not str(todo.id) in [y.target for y in request.user.messagebox.message_set.all().filter(target=str(todo.id))]:
            message = Message()
            message.box = request.user.messagebox
            message.target = str(todo.id)
            message.content = '마감일이 지났습니다.'
            message.save()

    return render(request, 'app_todo/index.html', {'todo_list': todo_list, 'today': today})


def complete_index(request):
    todo_list = request.user.todo_set.all().filter(isFinish='Yes')
    return render(request, 'app_todo/dead_index.html', {'todo_list': todo_list , 'headline': '완료된 목록'})


def deadline_index(request):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    todo_list = request.user.todo_set.all().filter(isFinish='no', deadline=today)
    return render(request, 'app_todo/dead_index.html', {'todo_list': todo_list, 'headline': '오늘 마감인 목록'})


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'app_todo/detail.html', {'todo': todo})


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        try:
            todo.title = request.POST.get('title')
            todo.content = request.POST.get('content')
            todo.deadline = request.POST.get('deadline')
            todo.save()
            return redirect('app_todo:detail', todo.id)
        except:
            pass
    return render(request, 'app_todo/edit.html', {'todo': todo})


def new(request):
    if request.method == "POST":
        todo = Todo()
        todo.author = request.user
        todo.title = request.POST.get('title')
        todo.content = str(request.POST.get('content')).strip()
        print(request.POST.get('deadline'))
        if request.POST.get('deadline') != '':
            todo.deadline = request.POST.get('deadline')
        todo.priority = len(request.user.todo_set.all().filter(isFinish='no'))+1
        todo.save()
        return redirect('app_todo:index')
    return render(request, 'app_todo/new.html')


def delete(request, pk):
    todo_list = request.user.todo_set.all().filter(isFinish='no', pk__gt=pk)
    for todo in todo_list:
        todo.priority -= 1
        todo.save()
    Todo.objects.get(pk=pk).delete()
    return redirect('app_todo:index')


def finish(request):
    todo = Todo.objects.get(pk=request.GET.get('pk'))
    todo_list = request.user.todo_set.all().filter(pk__gt=request.GET.get('pk'))
    for todos in todo_list:
        todos.priority -= 1
        todos.save()
    todo.isFinish = 'Yes'
    todo.save()
    return JsonResponse({'message': 'OK'})


def changePriority(request, pk):
    todo = Todo.objects.get(pk=pk)
    try:
        if request.GET.get('arrow') == 'down':
            next = list(request.user.todo_set.all().filter(isFinish='no', priority__gt=todo.priority).order_by('priority'))[0]
            print(list(request.user.todo_set.all().filter(isFinish='no', priority__gt=todo.priority).order_by('priority')))
            print(next)
        else:
            next = list(request.user.todo_set.all().filter(isFinish='no', priority__lt=todo.priority).order_by('priority'))[-1]
        temp = todo.priority
        todo.priority = next.priority
        next.priority = temp
        next.save()
        todo.save()
    except:
        pass
    return JsonResponse({'message': 'OK'})