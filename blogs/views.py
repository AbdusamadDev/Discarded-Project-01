from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)

from blogs.models import BlogsModel
from blogs.forms import BlogsCreationForm, EditBlogForm


def homepage(request):
    return render(request, "Homepage.html", {})


class CreateBlogsView(CreateView):
    """Creating blogs goes here."""
    model = BlogsModel
    template_name = "blogs/create.html"
    form_class = BlogsCreationForm
    success_url = reverse_lazy("home")

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
            self.model(title=title, content=content, image=image).save()
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponse(str(form.errors))


class BlogsListView(ListView):
    """List of all recorded data"""

    model = BlogsModel
    queryset = BlogsModel.objects.all()
    template_name = "blogs/list.html"
    context_object_name = "object"


class EditBlogView(UpdateView):
    model = BlogsModel
    template_name = "blogs/edit.html"
    form_class = EditBlogForm
    success_url = reverse_lazy("home")
    pk_url_kwarg = "pk"


class DeleteBlogView(DeleteView):
    template_name = "blogs/blogsmodel_confirm_delete.html"
    model = BlogsModel
    queryset = BlogsModel.objects.all()
    success_url = reverse_lazy("list")
    pk_url_kwarg = "pk"


class DetailedBlogView(DetailView):
    template_name = "blogs/details.html"
    model = BlogsModel
    queryset = BlogsModel.objects.all()
    pk_url_kwarg = "pk"
