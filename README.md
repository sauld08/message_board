# Message Board

Este proyecto es una aplicación web construida con Django para gestionar una lista de tareas.

## Características
- Listado de tareas con título, fecha de creación y actualización.
- Interfaz sencilla usando Django y SQLite.

## Instalación
1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:
	```bash
	pip install -r requirements.txt
	```
3. Aplica migraciones:
	```bash
	python manage.py migrate
	```
4. Ejecuta el servidor de desarrollo:
	```bash
	python manage.py runserver
	```

## Uso
Accede a `http://localhost:8000/` para ver la lista de tareas.

## Estructura principal
- `tasks/`: App principal con modelos, vistas y URLs.
- `templates/`: Contiene la plantilla `tasks_list.html` para mostrar las tareas.
- `django_base/`: Configuración base del proyecto.
- `db.sqlite3`: Base de datos SQLite.

## Requisitos
- Python 3.11+
- Django 5.2.6

## Licencia
Uso educativo.
