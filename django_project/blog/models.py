from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from os.path import splitext
import os

def unique_file_path(instance, filename):
    instance.original_file_name = filename

    # Get new file name/upload path
    base, ext = splitext(filename)
    newname = "image.jpg"
    return os.path.join('ml', newname)

class Take_Img(models.Model):
    image = models.ImageField(upload_to=unique_file_path)



class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    state = models.CharField(max_length=18, default='any')
    price = models.IntegerField()
    post_image = models.ImageField(default='default.jpg', upload_to='post_pics')
    post_image2 = models.ImageField(default='default.jpg', upload_to='post_pics')
    post_image3 = models.ImageField(default='default.jpg', upload_to='post_pics')
    post_image4 = models.ImageField(default='default.jpg', upload_to='post_pics')
    post_image5 = models.ImageField(default='default.jpg', upload_to='post_pics')
    post_image6 = models.ImageField(default='default.jpg', upload_to='post_pics')


    author = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post2(models.Model):

    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(default='default.jpg', upload_to='post2_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
