from django.db import models

# Create your models here.
class Job(models.Model):
    #Image
    image = models.ImageField(upload_to='images/')
    #Summary
    summary = models.CharField(max_length=200)
    #Title
    title = models.CharField(max_length=20)
    #detail
    detail = models.TextField(null= True)
    #Link

    def __str__(self):
        return self.summary