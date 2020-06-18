from django.db import models


class CustomerChecker(models.Model):
    customer_name = models.CharField(max_length=100)

    class Meta:
        app_label = 'customers'

    def __str__(self):
        return self.customer_name
