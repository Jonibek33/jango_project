from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"POST: ${self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"