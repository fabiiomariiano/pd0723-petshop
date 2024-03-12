import pytest
from rest_api.serializers import AgendamentoSerializer
from reserva.models import Petshop
from model_bakery import baker
from datetime import date, timedelta

@pytest.fixture
def dados_agendamento_data_no_passado():
  ontem = date.today() - timedelta(days=1)
  petshop = baker.make(Petshop)
  dados = {
    'nomeDoPet': 'Budy',
    'nomeDoDono': 'Fabio',
    'telefone': '819999999',
    'data': ontem,
    'observacoes': 'Ele está muito sujo!',
    'tamanho': 0,
    'turno': 'tarde',
    'petshop': petshop.pk
  }

  return dados

@pytest.mark.django_db
def test_agendamento_serializer_data_invalida(dados_agendamento_data_no_passado):
  serializer = AgendamentoSerializer(data=dados_agendamento_data_no_passado)
  assert not serializer.is_valid()
