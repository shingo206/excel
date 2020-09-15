from django.db import models


# Create your models here.
class Log(models.Model):
    title = models.CharField(max_length=100, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
