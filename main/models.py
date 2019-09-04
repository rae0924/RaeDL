from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    on_portfolio = models.BooleanField(default=False)
    page_url_name = models.CharField(max_length=100, default='raedl-home')
    github_link = models.URLField(default='https://github.com/rae0924')

    def __str__(self):
        return self.title
