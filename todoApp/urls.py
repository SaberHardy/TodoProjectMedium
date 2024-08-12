from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ViewTodo.as_view(), name='index'),
    # path('detail_todo/<int:id>/', views.detail_todo, name='detail'),
    path('detail_todo/<int:pk>/', views.DetailTodo.as_view(), name='detail_todo'),
    path('update_todo/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('create_todo/', views.CreateTodo.as_view(), name='create_todo'),
]
