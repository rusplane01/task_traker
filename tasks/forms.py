from django import forms
from tasks.models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'descrtiption',
            'status',
            'priority',
            'due_date',
            'creator',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'media']
        widgets = {
            "media": forms.FileInput()
        }