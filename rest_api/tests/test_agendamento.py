from rest_framework.test import APIClient
import pytest
from model_bakery import baker
from reserva.models import Reserva, Petshop
from datetime import date, timedelta

@pytest.fixture
def agendamento():
  return baker.make(Reserva)

@pytest.fixture
def dados_agendamento():
  amanha = date.today() + timedelta(days=1)
  petshop = baker.make(Petshop)
  dados = {
    'nomeDoPet': 'Budy',
    'nomeDoDono': 'Fabio',
    'telefone': '819999999',
    'data': amanha,
    'observacoes': 'Ele está muito sujo!',
    'tamanho': 0,
    'turno': 'tarde',
    'petshop': petshop.pk
  }

  return dados

@pytest.fixture
def usuario():
  return baker.make('auth.User')

@pytest.mark.django_db
def test_listar_todos_agendamentos_deve_retornar_1(agendamento):
  client = APIClient()
  resposta = client.get('/api/agendamento/')

  assert len(resposta.data['results']) == 1

@pytest.mark.django_db
def test_criar_agendamento(dados_agendamento, usuario):
  client = APIClient()
  client.force_authenticate(usuario)

  resposta = client.post('/api/agendamento/', dados_agendamento)

  assert resposta.status_code == 201


@pytest.mark.django_db
def test_resgatar_agendamento(dados_agendamento, usuario):
  client = APIClient()
  client.force_authenticate(usuario)

  respostaCriar = client.post('/api/agendamento/', dados_agendamento)

  assert respostaCriar.status_code == 201

  respostaResgatar = client.get('/api/agendamento/1/')

  assert respostaResgatar.data['nomeDoPet'] == dados_agendamento['nomeDoPet']



@pytest.mark.django_db
def test_remover_agendamento(dados_agendamento, usuario):
  client = APIClient()
  client.force_authenticate(usuario)

  respostaCriar = client.post('/api/agendamento/', dados_agendamento)

  assert respostaCriar.status_code == 201




  respostaPrimeiroResgate = client.get('/api/agendamento/1/')

  assert respostaPrimeiroResgate.data['nomeDoPet'] == dados_agendamento['nomeDoPet']




  respostaDeletar = client.delete('/api/agendamento/1/')

  assert respostaDeletar.status_code == 204




  respostaSegundoResgate = client.get('/api/agendamento/1/')

  assert respostaSegundoResgate.status_code == 404

