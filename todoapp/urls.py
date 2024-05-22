from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update_task/<int:task_id>/", views.update_task, name="update_task"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    path("toggle_task_status/<int:task_id>/", views.toggle_task_status, name="toggle_task_status"),
    path("tags/", views.tags_list, name="tags_list"),
    path("update_tag/<int:tag_id>/", views.update_tag, name="update_tag"),
    path("delete_tag/<int:tag_id>/", views.delete_tag, name="delete_tag"),
]
