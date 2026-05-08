from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import AlunoModelForm
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

class AlunoAddView(SuccessMessageMixin, CreateView):
    model = Aluno
    form_class = AlunoModelForm
    template_name = 'alunos_form.html'
    success_url = reverse_lazy('alunos')
    success_message = 'Aluno cadastrado com sucesso!'

class AlunoUpdateView(SuccessMessageMixin, UpdateView):
    model = Aluno
    form_class = AlunoModelForm
    template_name = 'alunos_form.html'
    success_url = reverse_lazy('alunos')
    success_message = 'Aluno alterado com sucesso!'

class AlunoDeleteView(SuccessMessageMixin, DeleteView):
    model = Aluno
    template_name = 'alunos_apagar.html'
    success_url = reverse_lazy('alunos')
    success_message = 'Aluno excluído com sucesso!'