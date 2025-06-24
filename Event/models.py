from django.db import models

# Create your models here.

category_list=(('sport','sport'),
               ('musique','musique'),
               ('Cinema','Cinema'))

class Event(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    category =models.CharField(choices=category_list ,max_length=20)
    image = models.ImageField(null=True)
    state= models.BooleanField(default=True)
    nbr_participants= models.IntegerField()
    evt_date= models.DateTimeField()
    creation_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    