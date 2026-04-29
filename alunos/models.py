from django.db import models
from django.db.models.functions import Upper
from stdimage import StdImageField

class Usuario(models.Model):
    nome = models.CharField('Nome',max_length=50, help_text='Nome Completo')
    email = models.EmailField('E-mail',max_length=100, help_text='Endereço de e-mail', unique=True)
    fone = models.CharField('Telefone',max_length=15, help_text='Número de telefone')
    foto = StdImageField('Foto',upload_to='usuarios', delete_orphans=True, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class Aluno(Usuario):
    plano = models.CharField('Plano',max_length=100, help_text='Plano do aluno')
    validadePlano = models.DateField('Validade plano', help_text='Data do término do plano')
    endereco = models.CharField('Endereço', max_length=100, help_text='Endereço completo')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return super().nome