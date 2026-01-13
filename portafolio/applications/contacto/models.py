from django.db import models
#
from model_utils.models import TimeStampedModel
# Create your models here.


class Contacto(TimeStampedModel):
    nombre_completo = models.CharField(
        'Nombre Completo',
        max_length=255        
    )
    email = models.EmailField(
        'Correo Electronico'
    )
    asunto = models.CharField(
        'Asunto',
        max_length=255
    )
    mensaje = models.TextField(
        'Mensaje'
    )
    leido = models.BooleanField(
        'Mensaje Leido',
        default=False
    )


    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['id']
    

    def __str__(self):
        return f'{self.nombre_completo} {self.asunto}'