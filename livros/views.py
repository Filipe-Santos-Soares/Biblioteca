from django.shortcuts import render
from rest_framework import viewsets # viewsets do DRF para CRUD automático
from .models import Autor, Livro # modelos usados nas views
from .serializers import AutorSerializer, LivrosSerializer # serializers para (de)serializar os
from django_filters.rest_framework import DjangoFilterBackend # permite filtragem via query parametros 

# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all() # queryset base usado pelo ViewSet
    serializer_class = AutorSerializer # serializer que define representação e validação

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all() # queryset base para operações do ViewSet
    serializer_class = LivrosSerializer # queryset base para operações do ViewSet
    filterset_fields = ['titulo', 'autor__nome', 'isbn', 'ano']