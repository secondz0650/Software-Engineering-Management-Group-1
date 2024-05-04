from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    harvest = models.CharField(max_length=500, null=False, blank=False)
    Fertilizer = models.CharField(max_length=500, null=False, blank=False)
    cultivate = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
