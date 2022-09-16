from django.urls import path

from . import views

urlpatterns = [
    path("", views.projects_list, name="projects-list"),
    path("<uuid:id>/", views.project_detail, name="project-detail"),
    path("tags/", views.tags_list, name="tag-list"),
]
