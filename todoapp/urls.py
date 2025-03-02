from django.urls import path
from .views import deleteTodo, index, about, updateTodo

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('delete-todo/<int:id>/', deleteTodo, name="deleteTodo"),
    path('update/<int:id>/', updateTodo, name='updateTodo'),
]
