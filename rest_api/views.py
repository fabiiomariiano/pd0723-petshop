from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from reserva.models import Reserva, Petshop
from base.models import Contato
from rest_api.serializers import AgendamentoSerializer, ContatoSerializer, PetshopSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class PetshopModelViewSet(ReadOnlyModelViewSet):
  queryset = Petshop.objects.all()
  serializer_class = PetshopSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  authentication_classes = [TokenAuthentication]

class AgendamentoModelViewSet(ModelViewSet):
  queryset = Reserva.objects.all()
  serializer_class = AgendamentoSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  authentication_classes = [TokenAuthentication]

class ContatoModelViewSet(ModelViewSet):
  queryset = Contato.objects.all()
  serializer_class = ContatoSerializer
  permission_classes = [IsAuthenticated]
  authentication_classes = [TokenAuthentication]


@api_view(['GET', 'POST'])
def hello_world(request):
  if request.method == 'POST':
    name = request.data.get('name')
    age = request.data.get('age')
    return Response({ 'message': f'Olá, {name}, seja bem-vindo! Você atualmente está com {age} anos'})

  return Response({ 'message': 'Hello World!!'})
