from django import forms

from app_todo.models import Todo


class TodoInputForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'content',)
