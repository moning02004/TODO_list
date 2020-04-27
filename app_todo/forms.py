from django import forms

from app_todo.models import Todo


class TodoInputForm(forms.ModelForm):
    PRIORITY = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3)
    ]

    title = forms.CharField(label='제목')
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={'resize': 'none'}))
    deadline = forms.DateField(label='기한', required=False, widget=forms.DateInput(), help_text='YYYY-mm-dd')
    priority = forms.IntegerField(label='중요', required=False, widget=forms.RadioSelect(choices=PRIORITY))

    class Meta:
        model = Todo
        fields = ('title', 'content', 'deadline', 'priority')
