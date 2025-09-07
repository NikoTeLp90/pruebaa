
from django.urls import path
from .views import *


urlpatterns = [

    ##Login
    path('login/', PersonaLoginView.as_view(), name='login'),
    
    path('', HomeView.as_view(), name='home'),
    path('administracion/', AdministracionView.as_view(), name='administracion'),

    ##ABM PERSONAS
    path('personas/', PersonaListView.as_view(), name='persona_list'),
    path('personas/nueva/', PersonaCreateView.as_view(), name='persona_create'),
    path('personas/<int:pk>/editar/', PersonaUpdateView.as_view(), name='persona_update'),
    path('personas/<int:pk>/eliminar/', PersonaDeleteView.as_view(), name='persona_delete'),

    ##ABM Rol
    path('rol/', RolListView.as_view(), name='rol_list'),
    path('rol/nueva/', RolCreateView.as_view(), name='rol_create'),
    path('rol/<int:pk>/editar/', RolUpdateView.as_view(), name='rol_update'),
    path('rol/<int:pk>/eliminar/', RolDeleteView.as_view(), name='rol_delete'),

    
]