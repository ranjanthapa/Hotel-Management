from django.contrib.auth.models import User
from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.position}'
