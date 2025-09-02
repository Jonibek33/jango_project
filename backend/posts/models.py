from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(default='posts_pics/default.png', upload_to='posts_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"POST: ${self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"