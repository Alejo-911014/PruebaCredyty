# PruebaCredyty

# CRUD

El siguiente crud en un ejemplo de creación de usuarios 
se debe instalar los requerimientos con
pip install -r requirements.txt
correr los comandos: 
python manage.py migrate
python manage.py makemigrations
crear un usuario
python manage.py createsuperuser
e iniciar
python manage.pu runserver

# END

En el repositorio se encuentran 5 archivos py correspondientes a la solución de los 5 puntos nivel semi-senior.
Cada punto fue solucionado y comentado con las librerias internas de python 3 en su versión 3.7 por lo que no hay necesidad de requerimientos.

## Revisiones

### Punto 4
  La ejecución de este scrips es una recurrencia que dependiendo de la maquina puede tardar de 4 a 8 horas de ejecución.
  Su solución esta escrita como comentario dentro del archivo punto4.py y su resultado como archivo de texto.
  
### Punto 5
  La solución no puede ser encontrada debido al gran procesamiento que requiere. Pero al ejecutan 100 filas el resultado es el mismo del ejemplo
  
# Docker

La ejecución de Docker consiste en la creación de los containers con el comando (en linux)
docker build -t python-p1 .
docker build -t python-p2 .
docker build -t python-p3 .
docker build -t python-p4 .
docker build -t python-p5 .

y su continua ejecución con docker run python-p1  

El archivo Dockerfile(2) contiene el script para ejecutar build del punto 3 debido a que debe añadirse el keylog.txt
