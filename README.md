# Proyecto Módulo 7
Sistema de administración de productos para una tienda de emociones (e-commerce).


## Motor de base de datos utilizado
**El proyecto utiliza PostgreSQL como motor de base de datos relacional, administrado a través de DBeaver**


## Descripción del modelo de datos
El sistema cuenta con un único modelo que representa el catálogo de productos del e-commerce.

|      Campo     |      Tipo      |       Descripción         |      Validaciones   | 
|----------------|----------------|---------------------------|---------------------| 
|       id       |    AutoField   |   Identificador único     | Auto-incrementable  | 
|     nombre     | CharField(100) |   Nombre del producto     |     Obligatorio     |
|  descripcion   |    TextField   |  Descripción detallada    |     Obligatorio     |
|     precio     |  IntegerField  |      Precio en pesos      |      Mayor a 0      |
|     imagen     | CharField(200) |     Ruta de la imagen     |      Opcional       |
|      stock     |  IntegerField  | Cantidad disponible (≥ 0) |   Mayor 0 igual a 0 |
| fecha_creacion |  DateTimeField |     Fecha de creación     |     Automático      |


## Rutas principales del módulo de administración

|            URL           |  Método  |        Funcionalidad     |         Acceso        |
|--------------------------|----------|--------------------------|-----------------------|
|             /            |    GET   |    Listado de productos  |        Público        |
|          /login/         | GET/POST |       Iniciar sesión     |        Público        |
|         /logout/         |    GET   |       Cerrar sesión      | Usuarios autenticados |
|     /products/create/    | GET/POST |      Crear producto      |    Administradores    |
|   /products/edit/<id>/   | GET/POST |     Editar producto      |    Administradores    |
|  /products/delete/<id>/  | GET/POST |    Eliminar producto     |    Administradores    |
|         /admin/          |    GET   |  Panel de administración |    Administradores    |


## Usuarios de prueba
**admin / admin123 (Superusuario)**


## Pasos para ejecutar el proyecto

# 1. Activar entorno virtual
env\Scripts\activate  # Windows
source env/bin/activate  # Linux/macOS

# 2. Instalar dependencias
pip install django psycopg2-binary

# 3. Configurar PostgreSQL (crear base de datos 'portafolio_m7')
El proyecto necesita carga de DB para su funcionamiento, se adjunta información de prueba en la parte inferior del presente archivo

# 4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser

# 6. Ejecutar servidor
python manage.py runserver


----------------------------------------------------------------------
----------------------------------------------------------------------

## Configuración DB

CREATE DATABASE portafolio_m7
    ENCODING 'UTF8'
    LC_COLLATE 'C'
    LC_CTYPE 'C'
    TEMPLATE template0;

## DATOS DE PRUEBA
Cargar por medio del comando 
**python manage.py shell**


from products.models import Producto

productos = [
    Producto(nombre="Felicidad Premium", descripcion="La emoción más buscada.", precio=9990, imagen="assets/Felicidad.png", stock=10),
    Producto(nombre="Tristeza + Consuelo", descripcion="Para esos días grises.", precio=4990, imagen="assets/Tristeza.png", stock=15),
    Producto(nombre="Ira Extrema", descripcion="Ideal para liberar estrés.", precio=7990, imagen="assets/Furia.png", stock=8),
    Producto(nombre="Miedo Absoluto", descripcion="Enfrenta tus miedos.", precio=14990, imagen="assets/Miedo.png", stock=5),
    Producto(nombre="Calmación Total", descripcion="Alcanza la paz interior.", precio=59990, imagen="assets/Calmación.png", stock=3),
    Producto(nombre="Emoción Secreta", descripcion="Una sorpresa emocional única.", precio=22990, imagen="assets/Suerte.png", stock=7),
]

Producto.objects.bulk_create(productos)
print(f"Productos creados: {Producto.objects.count()}")
exit()