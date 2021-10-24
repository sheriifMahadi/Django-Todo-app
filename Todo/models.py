from django.db import models
from django.db.models import Q


# Create your models here.
class Task(models.Model):
    """Model for the task the user wants to enter"""
    task = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        """Return a string rep of the model"""
        return (self.task)

