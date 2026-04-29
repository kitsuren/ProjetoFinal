from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Aluno

class AlunosView(ListView):
    model = Aluno
    template_name = 'alunos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(AlunosView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem alunos cadastrados!')