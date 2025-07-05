from django.contrib import admin

from .models import *
# Register your models here.





class ParticipationInline(admin.TabularInline):
    
    model = Participants
    
    extra=20



class numberOfParticipantsFilter(admin.SimpleListFilter):
    
    title="Number of participants"

    parameter_name='nbr'
    
    
    def lookups(self,request,model_admin):
        
        return (('No',('No participants')) , 
                ('Yes',('There are participants'))
                )
        
        
    def queryset(self,request,queryset):
        if self.value()=="No":
            
            return queryset.filter(nbr_participants__exact=0)
        
        if self.value()=="Yes":
            
            return queryset.filter(nbr_participants__gt=0)
        

def accept_state(ModelAdmin,request,queryset):
    
        queryset.update(state=True)



def refuse_state(ModelAdmin,request,queryset):
    
        queryset.update(state=False)


def change_category(ModelAdmin,request,queryset):
    
        queryset.update(category="sport")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    
    search_fields=('title',)
    list_display= ('title','description','category', 'nbr_participants','state','evt_date','organisateur',)
    list_per_page=2
 
    actions=[accept_state, refuse_state , change_category]
    
    autocomplete_fields=['organisateur']
    
    
    list_filter=('category','state',numberOfParticipantsFilter)
    
    inlines =[ParticipationInline]









admin.site.register(Participants)