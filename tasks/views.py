from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from tasks import models
from tasks.mixins import UserisOwnerMixin
from tasks.forms import TaskForm, CommentForm
from django.urls import reverse_lazy

class TaskListView(ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = "tasks/task_list.html"

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Додаємо порожню форму коментаря в контекст
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()
            return redirect('task-detail', pk=comment.task.pk)
        else:
            # Тут можна обробити випадок з невалідною формою
            pass

class TaskCreateView(CreateView):
    model = models.Task
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

