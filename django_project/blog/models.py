from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    imagePost = models.ImageField(default='default.jpg',upload_to='post_pics')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        imagePost = Image.open(self.imagePost.path)

        if imagePost.height > 0 and imagePost.width > 0:
            output_size = (500,500)
            imagePost.thumbnail(output_size)
            imagePost.save(self.imagePost.path)
    
    
