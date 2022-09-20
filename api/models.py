from django.db import models

class ItemBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField
    class Meta:
        abstract = True



class User(ItemBase):
    avatar  = models.ImageField(upload_to = 'upload/%Y/%m')
    

class Category(ItemBase):
    name = models.CharField(max_length=128, null=False, unique=True)

class Project(models.Model):
    image = models.ImageField(upload_to='project/%Y/%m')
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    
