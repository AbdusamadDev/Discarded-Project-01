from django.urls import path

from blogs import views

urlpatterns = [
    path("create/", views.CreateBlogsView.as_view(), name="create"),
    path("list/", views.BlogsListView.as_view(), name="list"),
    path("<int:pk>/edit/", views.EditBlogView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.DeleteBlogView.as_view(), name="delete"),
    path("<int:pk>/details/", views.DetailedBlogView.as_view(), name="details"),
]
