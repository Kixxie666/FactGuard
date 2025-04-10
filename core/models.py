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

    def downvote_count(self):
        return self.votes.filter(vote_type='downvote').count()

    def should_be_removed(self):
        return self.downvote_count() >= 1  # Remove if 1 downvote

class Vote(models.Model):
    VOTE_TYPES = [
        ('upvote', 'Upvote'),
        ('downvote', 'Downvote')
    ]

    post = models.ForeignKey(CommunityPost, related_name="votes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=VOTE_TYPES)
    
    class Meta:
        unique_together = ('post', 'user')  # no duplicate votes from the same user
