from django.db import models

# Create your models here.
class SSHUser(models.Model):
    username = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    feed_name = models.CharField(max_length=100)
    feed_event = models.CharField(max_length=30)

    def __set__(self):
        return self.username