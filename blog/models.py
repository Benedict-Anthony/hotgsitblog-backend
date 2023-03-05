from io import BytesIO
from django.db import models
from users.models import User
from PIL import Image
from django.core.files import File
from django.utils.text import slugify



    

class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True).order_by("-published_at")

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    publisher = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    excerpt = models.CharField(max_length=255, editable=False, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    objects = models.Manager()
    published = PostManager()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if len(self.body) >= 200:
            self.excerpt = self.body[0:199]
        else:
            self.excerpt = self.body
        return super().save(*args, **kwargs)
    
       
    def image_url(self):
        try:
        #    return f'https://hotgiostblogbackend.onrender.com{self.image.url}'
           return f'http://127.0.0.1:8000{self.image.url}'
        except:
            return ""
    def thumbnail_url(self):
        try:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return self.thumbnail.url
        except:
            return ""
        
    def make_thumbnail(self, image):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size=(300, 200))
        
        thumb_io = BytesIO()
        img.save(thumb_io, "PNG", quality=85)
        
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    

