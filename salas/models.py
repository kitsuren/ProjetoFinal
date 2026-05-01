from django.db import models

class Sala(models.Model):
    nome = models.CharField('Nome', max_length=100, help_text='Nome do sala', unique=True)
    tipo = models.CharField('Tipo', max_length=100, help_text='Tipo da sala')
    descricao = models.TextField('Descrição', max_length=300, help_text='Descrição e observações sobre a sala')

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def __str__(self):
        return self.nome
