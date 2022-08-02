from django.db import models

# Create your models here.
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/images', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title