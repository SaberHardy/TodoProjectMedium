from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail_todo/<int:id>/', views.detail_todo, name='detail'),
    path('update_todo/<int:id>/', views.update_todo, name='update'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),
    path('create_todo/', views.create_todo, name='create'),

]
