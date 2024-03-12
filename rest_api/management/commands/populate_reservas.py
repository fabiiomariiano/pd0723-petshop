from django.core.management.base import BaseCommand
from model_bakery import baker
from reserva.models import Reserva

class Command(BaseCommand):
  help = 'Criar dados fakes para a API de agendamento'

  def handle(self, *args, **options):
    total = 100

    self.stdout.write(
      self.style.WARNING(f'Criando {total} reservas!')
    )

    for i in range(total):
      self.stdout.write(
        self.style.HTTP_INFO(f'Criando reserva número: {i + 1}')
      )
      reserva = baker.make(Reserva)
      reserva.save()


    self.stdout.write(
      self.style.SUCCESS('Todas as reservas foram geradas com sucesso!!!!')
    )
    
    