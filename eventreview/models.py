from django.db import models
from django.contrib.auth.models import User
from events.models import Events


class EventReviews(models.Model):
    RATING = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Bad', 'Bad'),
        ('Horrible', 'Horrible')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../event_cn9ezb.jpg', blank=True
    )
    rating = models.CharField(
        max_length=50, choices=RATING, default='Average'
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f"{self.owner}'s review"
