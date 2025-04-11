from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.png')

    def __str__(self):
        return self.user.username


class SavedWebsite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    legit_votes = models.IntegerField(default=0)
    fake_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.url


class CommunityPost(models.Model):
    url = models.URLField(unique=True)
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def fake_vote_count(self):
        return self.votes.filter(vote_type='fake').count()

    def should_be_removed(self):
        return self.fake_vote_count() >= 10  # Remove after 10 fake votes


class Vote(models.Model):
    VOTE_TYPES = [
        ('legit', 'Legit'),
        ('fake', 'Fake')
    ]

    post = models.ForeignKey(CommunityPost, related_name="votes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    vote_type = models.CharField(max_length=10, choices=VOTE_TYPES)

    class Meta:
        unique_together = ('post', 'user')  # No duplicate votes from the same user
