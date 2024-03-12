from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, PrimaryKeyRelatedField, ValidationError
from reserva.models import Reserva, Petshop
from base.models import Contato
from datetime import date

class PetshopSerializer(ModelSerializer):
  reservas = HyperlinkedRelatedField(
    many = True,
    read_only = True,
    view_name='api:reserva-detail'
  )

  class Meta:
    model = Petshop
    fields = '__all__'

class PetshopNestedModelSerializer(ModelSerializer):
  class Meta:
    model = Petshop
    fields = '__all__'

class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
  def __init__(self, **kwargs):
    self.serializer = PetshopNestedModelSerializer
    super().__init__(**kwargs)

  def use_pk_only_optimization(self):
    return False
  
  def to_representation(self, value):
    return self.serializer(value, context=self.context).data

class AgendamentoSerializer(ModelSerializer):
  petshop = PetshopRelatedFieldCustomSerializer(
    queryset = Petshop.objects.all(),
    read_only = False
  )

  class Meta:
    model = Reserva
    fields = '__all__'

  def validate_data(self, value):
    hoje = date.today()

    if value < hoje:
      raise ValidationError('Não é possível reservar um banho para uma data do passado!')

    return value


class ContatoSerializer(ModelSerializer):
  class Meta:
    model = Contato
    fields = '__all__'