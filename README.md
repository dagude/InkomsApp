# InkomsApp
WebApp de Inkoms


Activar el entorno virtual
.\venv\scripts\activate

instalar Django
pip install django

instalar dependencias
pip install -r .\requirements.txt

crear/Inicializar proyecto
django-admin startproject project_name
or py django-admin startproject usuarios

crear una aplicación
py manage.py startapp app_name

start project
py manage.py runserver

ORM - Se crean las clases en models y luego ejecutar al nivel del proyecto venv
py manage.py makemigrations app
py manage.py migrate

Test
py manage.py test app_name

crear super usuario
py manage.py createsuperuser