from django.contrib import admin

from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preço', 'estoque', 'slug', 'criado', 'modificado', 'ativo')
    search_fields = ('nome',)
# Register your models here.
