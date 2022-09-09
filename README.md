# Django_sistema_de_tareas_Basico
Proyecto básico de un sistema de tareas  con Django

En el archivo settings.py configurar su base de datos postgres

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tasksdb', #colocar la base de datos que creo
        'USER': 'postgres', # usuario
        'PASSWORD': '123456', # clave
        'HOST':'127.0.0.1', 
        'PORT': '5432',
    }
}
