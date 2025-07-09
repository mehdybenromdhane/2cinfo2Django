from django.db import models


from Person.models import Person

from datetime import datetime


category_list=(('sport','sport'),
               ('musique','musique'),
               ('Cinema','Cinema'))

class Event(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    category =models.CharField(choices=category_list ,max_length=20)
    image = models.ImageField(null=True , upload_to='images')
    state= models.BooleanField(default=True)
    nbr_participants= models.IntegerField(null=True)
    evt_date= models.DateTimeField()
    creation_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    organisateur = models.ForeignKey(Person, on_delete=models.SET_NULL , null=True)
    
    
    participant= models.ManyToManyField(Person, through="Participants" , related_name="participant") 
    def __str__(self):
        return self.title
    
    
    
    class Meta:
        
        constraints=[models.CheckConstraint(check=models.Q(evt_date__gt = datetime.now()) , name="Please check the event date")]
    
class Participants(models.Model):
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    
    participation_date= models.DateField(auto_now_add=True)
    
    
    class Meta:
         unique_together=["event","person"]
         
         verbose_name="Participant" 
   