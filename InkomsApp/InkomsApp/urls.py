"""InkomsApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include, re_path
from perfiles.views import SignUpView, BienvenidaView, SignInView, SignOutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    re_path(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    re_path(r'^inicia-sesion/$', SignInView.as_view(), name='sign_in'),
    re_path(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    # re_path(r'^cerrar-sesion/$', SignOutView.as_view(), name='new_password'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)