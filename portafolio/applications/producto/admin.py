from django.contrib import admin
#
from .models import Servicios, Proyecto, Habilidades
# Register your models here.


class ServiciosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'tipo_servicio',
        'descripcion',
        'icon',
        'is_active'
    )


admin.site.register(Servicios, ServiciosAdmin)


class ProyectoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'descripcion',
        'tecnologias',
        'imagen',
        'url'
    )


admin.site.register(Proyecto, ProyectoAdmin)



class HabilidadesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'nivel'
    )


admin.site.register(Habilidades, HabilidadesAdmin)