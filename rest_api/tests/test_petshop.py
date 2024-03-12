from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
def test_listar_todos_petshops_deve_retornar_lista_vazia():
  client = APIClient()
  resposta = client.get('/api/petshop/')

  assert len(resposta.data['results']) == 0
  assert resposta.data['count'] == 0