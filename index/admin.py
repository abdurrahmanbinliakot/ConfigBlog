from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Subscribe, Category, Post
# Register your models here.

admin.site.register(Subscribe)
admin.site.register(Category)

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'comment_count','view_count', 'featured','timestamp')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)