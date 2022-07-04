from django.contrib import admin

# Register your models here.
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    # fields to see in the admin intarface
    list_display = ('usuario', 'bio', 'web', 'sex')
