from django.contrib import admin
#
from .models import Contacto
# Register your models here.


class ContactoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_completo',
        'email',
        'asunto',
        'mensaje',
        'leido'
    )


admin.site.register(Contacto, ContactoAdmin)