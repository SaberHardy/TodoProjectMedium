from django.db import models
from django.urls import reverse

priorities = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
    ('N', 'None')
)


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=priorities)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')
