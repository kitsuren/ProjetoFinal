from django import forms
from .models import Aluno

class AlunoModelForm(forms.ModelForm):
  class Meta:
    model = Aluno
    fields = ['nome', 'fone', 'email', 'plano', 'validadePlano', 'endereco', 'foto']

    error_messages = {
        'nome': {'required': 'O nome do aluno é um campo obrigatório!'},
        'fone': {'required': 'O número do telefone é um campo obrigatório!'},
        'endereco': {'required': 'O endereço é um campo obrigatório!'},
        'plano': {'required': 'O plano do aluno é um campo obrigatório!'},
        'validadePlano': {'required': 'A validade do plano do aluno é um campo obrigatório!'},
        'email': {'required': 'O email do aluno é um campo obrigatório!',
                  'invalid': 'Formato inválido para o e-mail. Exemplo de formato válido: abc@def.com',
                  'unique': 'E-mail já cadastrado!'}
    }