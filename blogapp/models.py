from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=150)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField( upload_to='images/', height_field=None, width_field=None)
    
    def __str__(self):
        return self.title
    def descbody(self):
        return self.body[:100]+'.............................'
    