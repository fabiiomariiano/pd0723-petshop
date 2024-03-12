from django.db import models

# Create your models here.
class Reserva(models.Model):
  TAMANHO_OPCOES = (
    (0, 'Pequeno'),
    (1, 'Médio'),
    (2, 'Grande')
  )

  TURNO_OPCOES = (
    ('manha', 'Manhã'),
    ('tarde', 'Tarde')
  )

  nomeDoPet = models.CharField(verbose_name='Nome do PET', max_length=50)
  nomeDoDono = models.CharField(verbose_name='Nome do Dono', max_length=50)
  telefone = models.CharField(verbose_name='Telefone', max_length=15)
  data = models.DateField(verbose_name='Data')
  observacoes = models.TextField(verbose_name='Observações', blank=True)
  tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
  turno = models.CharField(verbose_name='Turno', max_length=10, choices=TURNO_OPCOES)
  petshop = models.ForeignKey(
    'Petshop',
    related_name = 'reservas',
    on_delete = models.CASCADE,
    blank = True,
    null = True
  )

  def __str__(self):
    return f'Dono: {self.nomeDoDono} - PET: {self.nomeDoPet} - Data da reserva: {self.data} - Turno: {self.turno}'

  class Meta:
    verbose_name = 'Reserva de Banho'
    verbose_name_plural = 'Reservas de Banhos'

class Petshop(models.Model):
  nome = models.CharField(verbose_name = 'Nome', max_length = 50)
  rua = models.CharField(verbose_name = 'Rua', max_length = 100)
  numero = models.CharField(verbose_name = 'Número', max_length = 10)
  bairro = models.CharField(verbose_name = 'Bairro', max_length = 50)

  def __str__(self):
    return f'Nome: {self.nome} - {self.rua}, {self.numero} - {self.bairro}'
  
  def qtd_reservas(self):
    return self.reservas.count()
  