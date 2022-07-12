from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import Http404
from django.views.generic import CreateView, TemplateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView 

from .models import Perfil

from .forms import SignUpForm

# Create your views here.
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se
        obtiene de él y usamos authenticate para que el usuario incie
        sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        
        return redirect('/')

class WelcomeView(TemplateView):
   template_name = 'perfiles/welcome.html'


class SignInView(LoginView):
    template_name = 'perfiles/sign_in.html'


class SignOutView(LogoutView):
    pass

class AboutView(TemplateView):
    template_name = 'perfiles/about.html'

def UserDetailView(request, username):
    try:
        User = Perfil.objects.get(id=username)
    except Perfil.DoesNotExist:
        raise Http404('perfil not found')
    return render(request, 'perfiles/user_detail.html', {
            'usuario': username,
            })
