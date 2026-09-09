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





## Pasos para ejecutar el proyecto

### 1. Activar entorno virtual
```bash
# Windows
env\Scripts\activate
# Linux/macOS
source env/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
Crea un archivo .env en la raíz del proyecto usando .env.example como plantilla y configura tus credenciales locales de PostgreSQL:
```Ini, TOML
SECRET_KEY=tu_clave_secreta_local
DEBUG=True
DB_NAME=portafolio_m7
DB_USER=postgres
DB_PASSWORD=tu_password_postgres
DB_HOST=localhost
DB_PORT=5432
```

### 4. Configurar PostgreSQL (crear base de datos 'portafolio_m7')
Ejecuta la siguiente consulta SQL en tu cliente de base de datos:
```sql
CREATE DATABASE portafolio_m7
    ENCODING 'UTF8'
    LC_COLLATE 'C'
    LC_CTYPE 'C'
    TEMPLATE template0;
```

### 5. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Cargar datos de prueba (OPCIONAL)
# Ejecuta consola
```bash
python manage.py shell
```

# E ingresa el siguiente script:
```python
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
```



### 8. Ejecutar servidor
```bash
python manage.py runserver
```

----------------------------------------------------------------------
----------------------------------------------------------------------
