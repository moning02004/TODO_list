from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic

from app_main.permissions import IsOwnerMixin
from .forms import TodoInputForm
from .models import Todo


class TodoListView(LoginRequiredMixin, generic.ListView):
    template_name = 'app_todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        todo_list = self.request.user.todo_set.all().order_by('is_finish', '-priority', 'deadline')
        type = self.request.GET.get('type')
        if type == 'progress':
            return todo_list.filter(Q(is_finish=False) & Q(deadline__gt=datetime.today()))
        if type == 'complete':
            return todo_list.filter(Q(is_finish=True))
        if type == 'today':
            return todo_list.filter(Q(is_finish=False) & Q(deadline=datetime.today()))
        return todo_list


class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('app_user:login')
    template_name = 'app_todo/new.html'
    form_class = TodoInputForm
    success_url = reverse_lazy('app_todo:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoDetailView(IsOwnerMixin, generic.DetailView):
    model = Todo
    context_object_name = 'todo'
    success_template_name = 'app_todo/detail.html'
    failed_template_name = 'app_todo/error.html'


class TodoUpdateView(IsOwnerMixin, generic.UpdateView):
    model = Todo
    context_object_name = 'todo'
    success_template_name = 'app_todo/edit.html'
    failed_template_name = 'app_todo/error.html'
    form_class = TodoInputForm
    success_url = reverse_lazy('app_todo:index')


class TodoDeleteView(IsOwnerMixin, generic.DeleteView):
    model = Todo
    failed_template_name = 'app_todo/error.html'
    success_url = reverse_lazy('app_todo:index')
