from django.contrib import admin
from .models import Mensaje

class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'mensaje')

admin.site.register(Mensaje, MensajeAdmin)