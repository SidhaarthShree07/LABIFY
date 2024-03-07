from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

class Post(models.Model):  
    title = models.CharField(max_length=80)
    lab = models.CharField(max_length=80)
    image = models.TextField()
    link = models.CharField(max_length=80)
    desc = models.TextField()
    proc = tinymce_models.HTMLField()
    show = models.ImageField(upload_to='images/', default='images/default.png')
    
    def __str__(self):
        return self.title

class Posting(models.Model):
    user = models.CharField(max_length=80)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user
