import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from app_user.models import Message
from .forms import TodoInputForm
from .models import Todo


def index_edit(request):
    todo_list = request.user.todo_set.all().filter(isFinish='no')
    today = datetime.datetime.now().strftime('%Y.%m.%d')
    return render(request, 'app_todo/index_edit.html', {'todo_list': todo_list, 'today': today})


def complete_index(request):
    todo_list = request.user.todo_set.all().filter(isFinish='Yes')
    return render(request, 'app_todo/dead_index.html', {'todo_list': todo_list, 'headline': '완료된 목록'})


def deadline_index(request):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    todo_list = request.user.todo_set.all().filter(isFinish='no', deadline=today)
    return render(request, 'app_todo/dead_index.html', {'todo_list': todo_list, 'headline': '오늘 마감인 목록'})


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        try:
            todo.title = request.POST.get('title')
            todo.content = request.POST.get('content')
            todo.deadline = request.POST.get('deadline') if request.POST.get('deadline') != '' else None
            todo.save()
            return redirect('app_todo:detail', todo.id)
        except:
            pass
    return render(request, 'app_todo/edit.html', {'todo': todo})


def delete(request, pk):
    todo_list = request.user.todo_set.all().filter(isFinish='no', priority__gt=Todo.objects.get(pk=pk).priority)
    for x in todo_list:
        x.priority -= 1
        x.save()
    todo = Todo.objects.get(pk=pk)
    Message.objects.get(target=todo.id).delete() if Message.objects.all().filter(target=todo.id).exists() else None
    todo.delete()
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
            next = \
                list(
                    request.user.todo_set.all().filter(isFinish='no', priority__gt=todo.priority).order_by('priority'))[
                    0]
        else:
            next = \
                list(
                    request.user.todo_set.all().filter(isFinish='no', priority__lt=todo.priority).order_by('priority'))[
                    -1]
        temp = todo.priority
        todo.priority = next.priority
        next.priority = temp
        next.save()
        todo.save()
    except:
        pass
    return JsonResponse({'message': 'OK'})


class TodoListView(LoginRequiredMixin, generic.ListView):
    queryset = Todo.objects.all()
    template_name = 'app_todo/index.html'
    context_object_name = 'todo_list'


class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('app_user:login')
    template_name = 'app_todo/new.html'
    form_class = TodoInputForm
    success_url = reverse_lazy('app_todo:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoDetail(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        view = TodoDetailView.as_view()
        return view(request, *args, **kwargs)


class TodoDetailView(LoginRequiredMixin, generic.DetailView):
    model = Todo
    template_name = 'app_todo/detail.html'
    context_object_name = 'todo'


class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Todo
    template_name = 'app_todo/edit.html'
    context_object_name = 'todo'
    form_class = TodoInputForm
    success_url = reverse_lazy('app_todo:index')


class TodoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('app_todo:index')
