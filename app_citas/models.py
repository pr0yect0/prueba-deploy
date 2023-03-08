from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes_posts')
    author = models.CharField(max_length=100)
    quote = models.TextField()
    likes=models.ManyToManyField(User, related_name='quotes_like',blank=True)

    def __str__(self):
        return f'{self.user}'
    def number_likes(self):
        return self.likes.count()