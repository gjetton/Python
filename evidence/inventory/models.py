from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid  # Import uuid module

class CustomUser(AbstractUser):
    # Add any custom user fields here
    pass

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    # Other fields...

class Item(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    disposition = models.CharField(max_length=255)
    digital_media = models.CharField(max_length=255)
    court_date = models.DateField()
    barcode = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # Other fields...

    def __str__(self):
        return self.name

