from django.contrib import admin

# Register your models here.
from .models import Person


# admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    
    search_fields=('username',)