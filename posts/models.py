from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/'
    )
    caption = models.CharField(max_length=255, blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} shared {self.caption}'
