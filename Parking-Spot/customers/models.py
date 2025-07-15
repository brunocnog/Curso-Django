from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField( # Faz a conexão da tabela de cliente com a de usuários do Django
        User,
        on_delete=models.PROTECT,
        blank=True, # Campos não obrigatórios usam blank=True e null=True
        null=True,
        related_name='customers',
        verbose_name='Usuário',
    )
    name = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=15, blank=True, null=True,unique=True, verbose_name='CPF',)
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone',)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em',)

# A classe Meta é um verbose name para tabela no caso Customers
class Meta:
    verbose_name = 'Cliente'
    verbose_name_plural = 'Clientes'

def __str__(self):
    return self.name