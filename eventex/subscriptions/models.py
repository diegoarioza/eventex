from django.db import models


class Subscriptions(models.Model):
    name = models.CharField(max_length=100)