from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "excerpt",)
    list_filter = ("is_published", "title",)
    

admin.site.register(Post, PostAdmin)
