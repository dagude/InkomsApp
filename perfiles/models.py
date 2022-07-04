from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.deletion import CASCADE


# Models.
class Perfil(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, null=False, blank=False, on_delete=CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    # about = models.TextField(null=True)
    # description = models.TextField(blank=True)
    web = models.URLField(blank=True)
    # created_on = models.DateTimeField('date created', auto_now_add=True)
    # birthday = models.DateField()
    # location = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to='profile_photos', null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)

    # Python 3
    def __str__(self): 
        return self.usuario.username

    # def name(self):
    #     return '{} {}'.format(self.first_name, self.last_name)

    # def __str__(self):
    #     return '{} {}'.format(self.first_name, self.last_name)


# En las últimas dos funciones hacemos uso de los signals específicamente 
# del post_save que lo que hace es crear el perfil después que un usuario
# es registrado, con esto aseguramos que el usuario tenga perfil.
# Puedes leer un poco mas sobre esta magia de django en la documentación
@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()
