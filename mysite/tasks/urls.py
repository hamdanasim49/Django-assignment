from django.urls import path

from . import views

app_name = "todolist"
urlpatterns = [
    path("", views.todoappView, name="todoappView"),
    path("submit", views.submit, name="submit"),
    path("Add/", views.detail, name="detail"),
    path("<int:item_id>/change/", views.change, name="change"),
    path("<int:item_id>/delete/", views.delete, name="delete"),
    path("<int:item_id>/update/", views.update, name="update"),
    path("<int:item_id>/edit/", views.edit, name="edit"),
]
