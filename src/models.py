from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=45)
    slug = models.CharField(max_length=15)
    description = models.TextField()
    created_at = models.DateField()
    author_name = models.TextField()

    def __str__(self):
        return self.title