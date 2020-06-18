from django.db import models


class Content(models.Model):
    app_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.app_name
