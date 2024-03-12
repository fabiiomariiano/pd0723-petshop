from django.contrib import admin
from reserva.models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
  list_display = ['nomeDoDono', 'nomeDoPet', 'data', 'turno', 'observacoes']
  search_fields = ['nomeDoDono', 'nomeDoPet']
  list_filter = ['data', 'turno', 'tamanho']