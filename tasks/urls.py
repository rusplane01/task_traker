from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task_create/', views.TaskCreateView.as_view(), name='task-create'),
    path('comment/edit/<int:pk>/', views.CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='delete-comment'),
    path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/complete/", views.TaskCompleteView.as_view(), name="task-complete"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
]

#app_name = 'tasks'