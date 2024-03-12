from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
  help = 'Cria um novo usuário e token para ele'

  def add_arguments(self, parser):
    parser.add_argument('--username', required=True)
    parser.add_argument('--password', required=True)

  def handle(self, *args, **options):
    username = options['username']
    password = options['password']

    self.stdout.write(
      self.style.HTTP_INFO(f'Criando um novo usuario para {username} com a senha {password}')
    )

    user = User(username=username)
    user.set_password(password)
    user.first_name = username
    user.save()

    self.stdout.write(
      self.style.SUCCESS('Usuário criado com sucesso!!')
    )

    self.stdout.write('Criando token para o usuário')

    token = Token.objects.create(user=user)

    self.stdout.write(
      self.style.SUCCESS(f'Token criado com sucesso: {token}')
    )



