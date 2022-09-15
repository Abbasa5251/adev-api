from django.urls import path

from .views import ProjectListView, TagListView

urlpatterns = [
    path("", ProjectListView.as_view(), name="project-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]
