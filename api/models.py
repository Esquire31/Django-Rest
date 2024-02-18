from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
