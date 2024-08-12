from django.urls import path

from . import views

urlpatterns = [
    path('', views.ViewTodo.as_view(), name='index'),
    path('detail_todo/<int:pk>/', views.DetailTodo.as_view(), name='detail_todo'),
    path('update_todo/<int:pk>/', views.UpdateTodo.as_view(), name='update_todo'),
    path('delete_todo/<int:pk>/', views.DeleteTodo.as_view(), name='delete_todo'),
    path('create_todo/', views.CreateTodo.as_view(), name='create_todo'),
]
