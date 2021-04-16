from django.contrib import admin
from core.models import Evento
# Register your models here.

class Evento_admin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario',)

admin.site.register(Evento, Evento_admin)
