from django.db import models

class Armario(models.Model):
    numero = models.CharField('Numero', max_length=5, help_text='Numero do armario', unique=True)

    class Meta:
        verbose_name = 'Armário'
        verbose_name_plural = 'Armários'

    def __str__(self):
        return self.numero