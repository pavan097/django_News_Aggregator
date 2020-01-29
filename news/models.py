from django.db import models


class NewsData(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    img = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title