from reserva.models import Reserva
from django import forms
from datetime import date

class ReservaForm(forms.ModelForm):
  class Meta:
    model = Reserva
    fields = '__all__'

    widgets = {
      'data': forms.DateInput(attrs={'type': 'date'}),
    }

  def clean_data(self):
    data = self.cleaned_data['data']
    hoje = date.today()

    if data < hoje:
      raise forms.ValidationError('Não é possível reservar um banho para uma data do passado!')
    
    quantidadeAtualDeReservas = Reserva.objects.filter(data=data).count()
    print(f'quantidade: {quantidadeAtualDeReservas}')

    if quantidadeAtualDeReservas >= 4:
      raise forms.ValidationError('O dia selecionado já está lotado. Selecione outro dia para a sua reserva!')

    return data