from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Jobs(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    requirement = models.TextField()
    location = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.position

    def get_absolute_url(self):
        return reverse('jobs-detail', kwargs={'pk': self.pk})
