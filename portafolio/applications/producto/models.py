from django.db import models
#
from model_utils.models import TimeStampedModel
# Create your models here.

class Servicios(TimeStampedModel):

    TIPOS_SERVICIOS = (
        ('web', 'Desarrollo Web'),
        ('ecommerce', 'E-commerce / Tiendas Online'),
        ('automation', 'Automatizaciones'),
        ('data', 'Análisis de Datos'),
        ('software', 'Software a Medida'),
    )


    titulo = models.CharField(
        'Titulo', 
        max_length=150
    )
    tipo_servicio = models.CharField(
        'Tipo de Servicio',
        max_length=20,
        choices=TIPOS_SERVICIOS
    )
    descripcion = models.TextField('Descripcion')
    icon = models.CharField(
        max_length=50,
        help_text="Ej: fa-solid fa-code"
    )
    is_active = models.BooleanField(
        'Servicio Activo', 
        default=True
    )


    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['id']
    

    def __str__(self):
        return self.titulo



class Proyecto(TimeStampedModel):
    titulo = models.CharField(
        'Titulo Proyecto', 
        max_length=200
    )
    descripcion = models.TextField('Descripcion')
    tecnologias = models.CharField(
        'Tecnologias Usadas', 
        max_length=255,
        help_text='Ej: Django, PostgeSQL, Pandas, Python, PowerBI'
    )
    imagen = models.ImageField(
        'Imagen', 
        upload_to='proyectos',
        blank=True, 
        null=True
    )
    url = models.URLField(
        'url Proyecto',
        blank=True, 
        null=True
    )


    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['id']

    
    def __str__(self):
        return self.titulo



class Habilidades(TimeStampedModel):
    nombre = models.CharField(
        'Nombre Habilidad', 
        max_length=100
    )
    nivel = models.PositiveIntegerField(
        'Nivel',
        help_text='Nivel de 1 a 100'
    )

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        ordering = ['id']
    

    def __str__(self):
        return self.nombre