from django.db import models

# Create your models here.

class Notes_Attributes(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-updated']