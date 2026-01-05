from django.db import models

class Comment(models.Model):

    name = models.CharField(max_length=255,null=False)
    score = models.IntegerField(default=3)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
