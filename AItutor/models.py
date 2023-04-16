from django.db import models

class session(models.Model):
    role = models.CharField(max_length=10)
    content = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)