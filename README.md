# employees-app
Sistema de empleados para la etapa 1 de la materia DSSD-Unlp
 
## Tecnologías

- Python 3
- Django Framework
- Django Rest Framework

## Guia de instalacion

Para poder correr localmente la aplicación hay ciertas dependencias que deben ser instaladas.
En primer lugar, es necesario tener Python 3.5/3.6/3.7, se puede chequear ejecutando python --v en la consola.

Utilizamos pip como gestor de paquetes.

- Django : pip install django
- Django Rest Framework : pip install djangorestframework

Dependiendo el motor de base de datos a utilizar, se deberá elegir entre diferentes paquetes, en nuestro caso MySQL requiere:

- MySQL : pip install mysql
- MySQL Client : pip install mysqlclient

Una vez que no queden dependencias por instalar (si es necesario otro paquete la consola lo indicará como feedback, junto con el comando necesario para instalarlo), hay que hacer las migraciones, para esto se ejecuta en orden:

- python manage.py migrate

## Guia de instalacion - Opcion Virtualenv

Sugerimos usar un entorno virtual de desarrollo como VirtualEnv o VirtualEnvWrapper.
Para instalarlos se debe ejecutar:

pip install virtualenv o pip install virtualenvwrapper respectivamente.

Una vez instalado, debe crearse un entorno siguiendo los pasos provistos en la documentacion

https://virtualenv.pypa.io/en/stable/

y luego, estando en la carpeta root de la aplicacion de Stock, se debe ejecutar:

pip install -r requirements.txt

## Corriendo la aplicación

Se debe levantar un server ejecutando el comando

'python manage.py runserver' (python puede reemplazarse por python3 dependiendo la instalación del mismo).

Ya se puede empezar a hacer requests a la api.
