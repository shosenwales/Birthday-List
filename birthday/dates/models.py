from django.db import models

# Create your models here.

class Birthdays(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title