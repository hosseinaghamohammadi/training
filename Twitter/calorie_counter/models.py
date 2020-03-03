from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    branded = models.BooleanField(default=False)
    per_gram = models.IntegerField(default=0)
    
    
    def __str__(self):
        if self.brand == None:
            return self.name
        else:
            return self.name + " " + self.brand
            
    
