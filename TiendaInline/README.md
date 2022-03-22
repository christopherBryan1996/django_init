Despues de crear el proyecto creamos una aplocacion ***python manage.py startapp gestionPedidos***.

Probamos que todo este bien con ***python manage.py check gestionPedidos***.

Para crear ya la base de datos: ***python manage.py makemigrations***.
Recordando que se esta usando SQL lite.

Para definir los models: ***python manage.py sqlmigrate gestionPedidos 0001***.
El 0001 es la version de migrate que se han realizado.

Para crear ya las tablas: ***python manage.py migrate*** 

Para crear un super usuario ***python manage.py createsuperuser***