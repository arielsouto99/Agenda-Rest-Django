from django.shortcuts import render

from django.views.generic import ListView, TemplateView

# Rest 
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
# Serializer
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    PersonaSerializer3,
    ReunionSerializer,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonPagination,
    CountReunionSerializer,
)

#
from .models import Person, Reunion

# Listar como veniamos haciendo
# Llamado a la base de datos, le pasa el contexto y lo muestra en el html
class ListaPersonas(ListView):
    template_name = "persona/personas.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


# Listar pero en API
class PersonListView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonView(TemplateView):
    template_name = "persona/lista.html"


# ListAPIView
class PersonSearchView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        # Filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains = kword
        )


# CreateAPIView
class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer


# RetrieveAPIView
class PersonDetailView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all() # Se puede filtrar


# DestroyAPIView
class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all() 


# UpdateAPIView
class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all() 

# RetrieveUpdateAPIView
class PersonRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all() 



class PersonApiLista(ListAPIView):
    """ Vista para intereactuar con serializadores """
    #serializer_class = PersonaSerializer
    #serializer_class = PersonaSerializer2
    serializer_class = PersonaSerializer3

    def get_queryset(self):
        return Person.objects.all()


class ReunionApiLista(ListAPIView):
    serializer_class = ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()


class ReunionApiListaLink(ListAPIView):
    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()

class PersonPaginationList(ListAPIView):
    """ Vista con paginacion """

    serializer_class = PersonaSerializer
    pagination_class = PersonPagination
  
    def get_queryset(self):
        return Person.objects.all()

class ReunioByPersonJob(ListAPIView):
    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()
    
    