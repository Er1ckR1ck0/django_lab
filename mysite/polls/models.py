from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    content = models.TextField()
    data_published = models.DateTimeField()

    # def __str__(self):
    #     return self.title
