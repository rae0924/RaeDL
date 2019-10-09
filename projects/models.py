from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    article_name = models.CharField(max_length=100)
    img_name = models.TextField()

    def __str__(self):
        return self.title



