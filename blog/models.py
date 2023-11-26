from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField((""))
    body = models.TextField((""))
    date = models.DateTimeField((""), auto_now=False, auto_now_add=True)
    # thumbnail
    # author