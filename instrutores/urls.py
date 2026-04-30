from django.urls import path
from .views import InstrutoresView, InstrutorAddView, InstrutorUpdateView, InstrutorDeleteView

urlpatterns = [
    path('instrutores', InstrutoresView.as_view(), name='instrutores'),
    path('instrutor/adicionar/', InstrutorAddView.as_view(), name='instrutor_adicionar'),
    path('<int:pk/instrutor/ediatr', InstrutorUpdateView.as_view(), name='instrutor_editar'),
    path('<int:pk>/instrutor/apagar/', InstrutorDeleteView.as_view(), name='instrutor_apagar'),
]