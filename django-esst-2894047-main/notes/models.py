from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=200)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
