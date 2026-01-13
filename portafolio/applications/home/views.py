from django.shortcuts import render
#
from django.views.generic import TemplateView
#
from applications.producto.models import Servicios, Habilidades
#
from applications.contacto.models import Contacto
#
from applications.contacto.forms import ContactoForm
#
from django.shortcuts import redirect
# Create your views here.


class IndexView(TemplateView):
    template_name = 'home/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Servicios.objects.all()
        context['skills'] = Habilidades.objects.all()
        context['form'] = ContactoForm    
        return context
    

    def post(self, request, *args, **kwargs):
        form = ContactoForm(request.POST)

        if form.is_valid():
            # 👈 AQUÍ se capturan los datos
            Contacto.objects.create(
                nombre_completo = form.cleaned_data['nombre_completo'],
                email = form.cleaned_data['email'],
                asunto = form.cleaned_data['asunto'],
                mensaje = form.cleaned_data['mensaje']
            )            
            
            return redirect('home_app:index')  # o una url de éxito

        # Si hay errores, se vuelve a renderizar con errores
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context) 
