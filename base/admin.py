from django.contrib import admin, messages

from base.models import Contato

@admin.action(description='Marcar como lido o(s) formulário(s)')
def marcar_como_lido(modeladmin, request, queryset):
  queryset.update(lido=True)
  modeladmin.message_user(request, 'Os formulário(s) de contato(s) foram marcado(s) como lido.', messages.SUCCESS)



@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'email', 'mensagem', 'data', 'lido']
  search_fields = ['nome', 'email']
  list_filter = ['data', 'lido']
  actions = [marcar_como_lido]
