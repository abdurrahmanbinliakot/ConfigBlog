from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.


class Subscribe(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# Category models
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# Post Model
class Post(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to ='post/thumbnail')
    overview = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default = 0)
    view_count = models.IntegerField(default = 0)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"id": self.id})
    