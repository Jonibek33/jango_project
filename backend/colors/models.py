from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Colors(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FRUIT: ${self.title}"

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'