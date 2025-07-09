from django.urls import path
from .views import *

urlpatterns = [
    path('hi/' , hello ),
    path('list/',listEvent, name="list"),
    path('affiche/', List.as_view()),
    path('details/<int:ide>',details , name="detailsEvent"),
    
    path('detailsClass/<int:pk>',DetailsEvent.as_view(),name="detailsClass"),
    
    path('delete/<int:idEvent>', delete , name="deleteEvent"),
    
    path('deleteClass/<int:pk>', DeleteEvent.as_view(), name="deleteWithClass"),
    path('participer/<int:ide>', participer, name="participe"),
    path('cancel/<int:ide>', cancel, name="cancel"),

    path('add/', AddEvent.as_view(), name="addEvent"),
    
    path('update/<int:pk>', UpdateEvent.as_view(), name="updateEvent")


]
