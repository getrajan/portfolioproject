from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None)
    summary = models.CharField( max_length=250)
    
    def __str__(self):
        return self.summary[:20]+"......."
    
