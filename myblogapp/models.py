from django.db import models
from datetime import datetime

# Create your models here.
class MyBlog(models.Model):
    title = models.CharField(max_length=50)
    body  = models.CharField(max_length=5000)
    created_at = models.DateTimeField(default=datetime.now)
