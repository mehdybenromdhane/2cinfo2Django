from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError
# Create your models here.

def validate_cin(value):
    
    if len(value) != 8:
        
        raise ValidationError("cin must has 8 characters")



def validate_email(value):
    
    if value.endswith("@esprit.tn") ==False:
        
        raise ValidationError("email must end with @esprit.tn")

        
class Person(AbstractUser):
    cin = models.CharField(primary_key=True , max_length=8 ,validators=[validate_cin])
    username=models.CharField(max_length=20,unique=True)

    email=models.EmailField(max_length=30 ,validators=[validate_email])
    
    USERNAME_FIELD="username"
    
    class Meta:
        verbose_name="Person"