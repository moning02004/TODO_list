from django.shortcuts import render, redirect
from django.template.defaultfilters import register


def index(request):
    if request.user.is_authenticated:
        return redirect('app_todo:index')
    return redirect('app_user:signup')


@register.filter
def add_class(field, cls):
    return field.as_widget(attrs={'class': cls})
