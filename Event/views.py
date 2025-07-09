from django.shortcuts import render,redirect


from .models import Event,Participants
# Create your views here.
from django.views.generic import *

from django.urls import reverse_lazy

from Person.models import Person

from .forms import EventForm

def hello(request):
    
    test = "Bonjour"

    return render(request , "event/hello.html" , { "abc":test})




def listEvent(request):
    
    events= Event.objects.filter(state=True)
    
    return render (request,'event/list.html',{"events":events})




class List(ListView):
    
    model= Event
    template_name="event/list.html"
    context_object_name="events"
    
    


def details(request,ide):
    
    
   btn = False 
   e1=  Event.objects.get(id=ide)
   
   
   p1 = Person.objects.get(cin=12345487)
   participation = Participants.objects.filter(event=e1, person=p1)
   
   if participation:
       btn = True
       
       
       
   return render(request,"event/details.html",{"event":e1 , "btn":btn})



class DetailsEvent(DetailView):
    model=Event
    context_object_name='event'
    
    template_name="event/details.html"
    
    
    

def delete(request,idEvent):
    
    event= Event.objects.get(id=idEvent)
    
    if event:
        event.delete()
        
        return redirect('list')
    
    
    
    
    
class DeleteEvent(DeleteView):
    model=Event
    
    success_url=reverse_lazy('list')
    template_name= "event/delete.html"
    
    
    
    
def participer(request , ide):
    
    e1= Event.objects.get(id=ide)    
    
    p1 = Person.objects.get(cin=12345487)
    
    participant = Participants.objects.create(event=e1 ,person=p1)
    
    if participant:
        participant.save()
        
        e1.nbr_participants+=1
        
        e1.save()
        
        return redirect('list')
        
    
    
def cancel(request , ide):
    
    e1= Event.objects.get(id=ide)    
    
    p1 = Person.objects.get(cin=12345487)
    
    participant = Participants.objects.filter(event=e1 ,person=p1)
    
    if participant:
        participant.delete()
        
        e1.nbr_participants-=1
        
        e1.save()
        
        return redirect('list')
    
    
    
    


class AddEvent(CreateView):
    model=Event
    form_class= EventForm
    template_name="event/add.html" 
    success_url=reverse_lazy('list')



class UpdateEvent(UpdateView):
     model=Event
     form_class= EventForm
     template_name="event/update.html" 
     success_url=reverse_lazy('list')