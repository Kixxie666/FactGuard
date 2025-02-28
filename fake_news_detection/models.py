from django.db import models
from django.contrib.auth.models import User


class SavedWebsite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
