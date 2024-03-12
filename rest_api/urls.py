from django.urls import path

from rest_framework.routers import SimpleRouter

from rest_api.views import hello_world, AgendamentoModelViewSet, ContatoModelViewSet, PetshopModelViewSet

app_name = 'rest_api'

router = SimpleRouter()
router.register('agendamento', AgendamentoModelViewSet)
router.register('contato', ContatoModelViewSet)
router.register('petshop', PetshopModelViewSet)

urlpatterns = [
  path('hello-world', hello_world, name='api-hello-world')
]

urlpatterns += router.urls