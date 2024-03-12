import pytest
from model_bakery import baker
from reserva.models import Reserva, Petshop
from datetime import date

def test_config():
  assert 1 == 1

@pytest.fixture
def reserva():
  data = date(2024, 3, 5)
  reserva = baker.make(Reserva, nomeDoDono='Fabio', nomeDoPet='Bud', data=data, turno='manha')
  return reserva


@pytest.mark.django_db
def test_str_de_reserva_deve_retornar_string_formatada(reserva):
  assert str(reserva) == 'Dono: Fabio - PET: Bud - Data da reserva: 2024-03-05 - Turno: manha'


@pytest.mark.django_db
def test_qtd_reservas_deve_retornar_reservas():
  petshop = baker.make(Petshop)
  
  quantidade = 5
  
  baker.make(
    Reserva,
    quantidade,
    petshop=petshop
  )

  assert petshop.qtd_reservas() == 5