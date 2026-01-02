from django.db import models

class Comments(models.Model):

    name = models.CharField(max_length=255,null=False)
    score = models.IntegerField(default=3)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
# Create your models here.
