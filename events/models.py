from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    CATEGORIES = [
        ('Food', 'Food'),
        ('Education', 'Education'),
        ('Job', 'Job'),
        ('Family', 'Family'),
        ('Culture', 'Culture'),
        ('Music', 'Music'),
        ('General', 'General')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/', default='../event_cn9ezb.jpg'
    )
    details = models.TextField(blank=True)
    date = models.DateField(blank=False)
    category = models.CharField(
        max_length=50, choices=CATEGORIES, default='General'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
