from django.db import models
from alunos.models import Usuario

class Instrutor(Usuario):
    especialidade = models.CharField('Especialidade', max_length=150, help_text='Especialidade do Instrutor')
    dataAdmissao = models.DateField('Admissão', help_text='Data de admissão do Instrutor')

    class Meta:
        verbose_name = 'Instrutor'
        verbose_name_plural = 'Instrutores'

    def __str__(self):
        return super().nome