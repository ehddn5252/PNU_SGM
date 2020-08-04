from django.db import models

# Create your models here.

class Users(models.Model):
    v1 = models.CharField(max_length=200)
    v2 = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.v1