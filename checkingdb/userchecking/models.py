from django.db import models


class UserChecker(models.Model):
    user_name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        app_label = 'userchecking'  # name of app

    def __str__(self):
        return self.user_name
