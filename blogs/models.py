from django.db import models


class BlogsModel(models.Model):
    """title, content, image, date created"""

    title = models.CharField(max_length=100, blank=False, null=False, unique=True, default="")
    content = models.TextField(max_length=8000, blank=False, null=False, unique=True, default="")
    image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return "Query: %s\n%s" % (self.title, self.content)

