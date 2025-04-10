from django.db import models
from django.contrib.auth.models import User
from core.models import SavedWebsite


class DetectionSavedWebsite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    legit_votes = models.IntegerField(default=0)
    fake_votes = models.IntegerField(default=0)