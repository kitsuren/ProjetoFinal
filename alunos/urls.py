from django.urls import path
from .views import AlunosView, AlunoAddView, AlunoUpdateView, AlunoDeleteView

urlpatterns = [
    path('alunos', AlunosView.as_view(), name='alunos'),
    path('aluno/adicionar', AlunoAddView.as_view(), name='aluno_adicionar'),
    path('<int:pk>/aluno/editar/', AlunoUpdateView.as_view(), name='aluno_editar'),
    path('<int:pk>/aluno/apagar/', AlunoDeleteView.as_view(), name='aluno_apagar'),
]