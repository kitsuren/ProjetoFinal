from django import forms
from .models import Instrutor

class InstrutorModelForm(forms.ModelForm):

    class Meta:
        model = Instrutor
        fields = ['nome', 'fone', 'email', 'especialidade', 'dataAdmissao', 'foto']

        error_messages = {
            'nome': {'required': 'O nome do instrutor é um campo obrigatório!'},
            'fone': {'required': 'O número do telefone é um campo obrigatório!'},
            'especialidade': {'required': 'A especialidade do instrutor é um campo obrigatório!'},
            'dataAdmissao': {'required': 'A data de admissão do instrutor é um campo obrigatório!'},
            'email': {'required': 'O email do instrutor é um campo obrigatório!',
                      'invalid': 'Formato inválido para o e-mail. Exemplo de formato válido: abc@def.com',
                      'unique': 'E-mail já cadastrado!'},
        }