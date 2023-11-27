from django.db import models

# Create your models here.
class Employee(models.Model):
    title = models.TextField()
    def __str__(self) -> str:
        return self.title