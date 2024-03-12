from pytest_django.asserts import assertTemplateUsed
import pytest
from datetime import date, timedelta
from model_bakery import baker
from reserva.models import Petshop, Reserva

@pytest.mark.django_db
def test_reserva_view_deve_retornar_template_correto(client):
  response = client.get('/reserva/criar/')

  assert response.status_code == 200
  assertTemplateUsed(response, 'criar_reserva_de_banho.html')


@pytest.fixture
def dados_reserva_valido():
  data_de_amanha = date.today() + timedelta(days=1)
  dados = {
    'nomeDoPet': 'Lua',
    'nomeDoDono': 'Liz',
    'telefone': '8199999999',
    'data': data_de_amanha,
    'tamanho': 0,
    'turno': 'tarde',
    'observacoes': '',
  }
  return dados

@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso_com_dados_corretos(client, dados_reserva_valido):
  response = client.post('/reserva/criar/', dados_reserva_valido)

  assert response.status_code == 200
  assert 'Reserva feita com sucesso' in str(response.content)


@pytest.mark.django_db
def test_reserva_sendo_criada_no_banco(client, dados_reserva_valido):
  response = client.post('/reserva/criar/', dados_reserva_valido)

  assert 'Reserva feita com sucesso' in str(response.content)

  assert Reserva.objects.all().count() == 1

  reserva = Reserva.objects.first()

  assert reserva.nomeDoPet == dados_reserva_valido['nomeDoPet']
  assert reserva.data == dados_reserva_valido['data']



