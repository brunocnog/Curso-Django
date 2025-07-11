from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255, verbose_name='Primeiro Nome')
    lastname = models.CharField(max_length=255, verbose_name='Sobrenome')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    gender = models.CharField(
        max_length=1,
        choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')],
        blank=True,
        null=True,
        verbose_name='Gênero'
    )
    address = models.TextField(blank=True, null=True, verbose_name='Endereço')
    # profile_picture = models.ImageField(upload_to='members/photos/', blank=True, null=True, verbose_name='Foto de Perfil')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['firstname']
        verbose_name = 'Membro'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
