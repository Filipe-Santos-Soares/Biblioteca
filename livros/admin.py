from django.contrib import admin
from .models import Autor, Livro
from rest_framework.authtoken.models import Token
# Register your models here.

# Admin para o modelo Autor: mostra o campo 'nome' e permite busca por nome
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome'] # colunas exibidas na listagem
    search_fields = ['nome'] # campos pesquisáveis

@admin.register(Livro)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'isbn', 'ano', 'paginas']
    search_fields = ['titulo', 'isbn']
    list_filter = ['ano', 'autor'] # filtros laterais

admin.site.register(Token)