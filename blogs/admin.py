from django.contrib import admin

from blogs.models import BlogsModel

# Register blogs model to Admin panel
admin.site.register(BlogsModel)
