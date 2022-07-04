from perfiles.views import SignUpView, HomeView, SignInView, SignOutView, AboutView, UserDetailView


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

# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

# handler404 = handler_404

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    re_path(r'^iniciar-sesion/$', SignInView.as_view(), name='sign_in'),
    re_path(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    # re_path(r'^nueva-contraseña/$', NewPassView.as_view(), name='new_password'),
    path('perfiles/<int:username>/', UserDetailView, name='user_detail'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
# urlpatterns += re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
# urlpatterns += url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)