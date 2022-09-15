from django.urls import path

from .views import projects_list, tags_list

urlpatterns = [
    path("", projects_list, name="projects-list"),
    path("tags/", tags_list, name="tag-list"),
]
