from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import Persona, Rol
from .forms import PersonaForm, RolForm, LoginForm
# Create your views here.

#Login
class PersonaLoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            persona = Persona.objects.get(email=email)
            if persona.check_password(password):
                self.request.session['persona_id'] = persona.id
                return redirect('home')  # Cambia por el nombre de tu vista principal
            else:
                form.add_error(None, "Contraseña incorrecta")
        except Persona.DoesNotExist:
            form.add_error(None, "Usuario no encontrado")
        return self.form_invalid(form)

#home y administracion
class HomeView(TemplateView):
    template_name = 'home.html'

class AdministracionView(TemplateView):
    template_name = 'administracion.html'

#ABM Personas
class PersonaListView(ListView):
    model = Persona
    template_name = 'personas/persona_list.html'
    context_object_name = 'personas'
    paginate_by = 10

class PersonaCreateView(CreateView):
    model = Persona
    template_name = 'personas/persona_form.html'
    form_class = PersonaForm
    success_url = '/crud/personas'

    def form_valid(self, form):
        persona = form.save(commit=False)
        raw_password = form.cleaned_data['password']
        persona.set_password(raw_password)
        return super().form_valid(form)

class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = 'personas/persona_form.html'
    form_class = PersonaForm
    success_url = '/crud/personas'

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'personas/persona_confirm_delete.html'
    success_url = '/crud/personas'


#ABM Rol
class RolListView(ListView):
    model = Rol
    template_name = 'rol/rol_list.html'
    context_object_name = 'roles'
    paginate_by = 10

class RolCreateView(CreateView):
    model = Rol
    template_name = 'rol/rol_form.html'
    form_class = RolForm
    success_url = '/crud/rol'


class RolUpdateView(UpdateView):
    model = Rol
    template_name = 'rol/rol_form.html'
    form_class = RolForm
    success_url = '/crud/rol'

class RolDeleteView(DeleteView):
    model = Rol
    template_name = 'rol/rol_confirm_delete.html'
    success_url = '/crud/rol'