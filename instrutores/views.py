from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import InstrutorModelForm
from .models import Instrutor

class InstrutoresView(ListView):
    model = Instrutor
    template_name = 'instrutores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(InstrutoresView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem

        else:
            return messages.info(self.request, 'Não existem instrutores cadastrados!')

class InstrutorAddView(SuccessMessageMixin, CreateView):
    model = Instrutor
    form_class = InstrutorModelForm
    template_name = 'instrutor_form.html'
    success_url = reverse_lazy('instrutores')
    success_message = 'Instrutor cadastrado com sucesso!'

class InstrutorUpdateView(SuccessMessageMixin, UpdateView):
    model = Instrutor
    form_class = InstrutorModelForm
    template_name = 'instrutor_form.html'
    success_url = reverse_lazy('instrutores')
    success_message = 'Instrutor alterado com sucesso!'

class InstrutorDeleteView(SuccessMessageMixin, DeleteView):
    model = Instrutor
    template_name = 'instrutor_apagar.html'
    success_url = reverse_lazy('instrutores')
    success_message = 'Instrutor excluído com sucesso!'

