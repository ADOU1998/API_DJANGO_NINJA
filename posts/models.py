from pyexpat import model
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=45)
    content=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
