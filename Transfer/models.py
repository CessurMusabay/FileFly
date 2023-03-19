from django.db import models


class Transfer(models.Model):
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=128)
    message = models.TextField()
    password = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
