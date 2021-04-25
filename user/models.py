from django.db import models
from django.contrib.auth.models import User

class Holiday(models.Model):
    name = models.CharField(
        max_length=255, null=True, blank=False, verbose_name="holiday name"
    )
    name_local = models.CharField(max_length=255, null=True, blank=False)
    language = models.CharField(max_length=255, null=True, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s"
    )
    description = models.TextField(
        null=True, blank=True, verbose_name="description about holiday"
    )
    country = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    date_year = models.CharField(max_length=10, blank=True, null=True)
    date_month = models.CharField(max_length=5, blank=True, null=True)
    date_day = models.CharField(max_length=5, blank=True, null=True)
    week_day = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name