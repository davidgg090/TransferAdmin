# Ejecución del Proyecto

## Configuración del Entorno Virtual:

1. Clona el repositorio de GitHub:
    ```
    git clone https://github.com/davidgg090/TransferAdmin.git
    ```
2. Accede al directorio del proyecto:
    ```
    cd TransferAdmin
    ```
3. Crea un entorno virtual para el proyecto:
    ```
    python -m venv venv
    ```
4. Activa el entorno virtual:

   En Windows:

   ```
   venv\Scripts\activate
   ```
   En macOS y Linux:

   ```
   source venv/bin/activate
   ```
   
## Instalación de Dependencias

Dentro del entorno virtual, instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

## Configuración del archivo .env
El archivo `.env` se utiliza para almacenar variables de entorno sensibles y configuraciones específicas de la 
aplicación. Debes crear este archivo en el directorio raíz del proyecto y agregar las siguientes variables:

```dotenv
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=localhost,127.0.0.1,testserver
```
   
## Creación de la Base de Datos
Para crear la base de datos localmente y ejecutar las migraciones:

   ```
   python manage.py migrate
   ```

## Ejecución de los Tests
Para ejecutar los tests:

   ```
   pytest
   ```

## Iniciar el Servidor de Desarrollo

Para iniciar el servidor de desarrollo:

```
python manage.py runserver
```

El servidor estará disponible en http://localhost:8000/.

## Ejecutar el Contenedor Docker (Opcional)

Construye la imagen de Docker:

```shell
docker build -t <nombre_de_la_imagen> .
docker run --env-file .env -p 8000:8000 nombre_imagen
```

## Documentación de la API
Para acceder a la documentación de la API, puedes utilizar los siguientes enlaces:

OpenAPI Schema: http://localhost:8000/api/schema/

Swagger UI: http://localhost:8000/api/schema/swagger-ui/

Redoc: http://localhost:8000/api/schema/redoc/

Estos enlaces te proporcionarán la documentación interactiva de la API, donde podrás explorar los endpoints disponibles
y probarlos directamente desde el navegador.

## Configuración del Registro (Logging)

Para configurar el registro de la aplicación, se ha definido un archivo `transferencias.log` donde se almacenarán los 
registros de nivel DEBUG de Django.

A continuación, se muestra la configuración de registro en el archivo `settings.py`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'transferencias.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```
Esta configuración establece que los registros de nivel DEBUG generados por Django se almacenen en el archivo 
transferencias.log.

Visualización de los Registros
Para ver los registros, sigue estos pasos:

Abre una terminal.
Accede al directorio donde se encuentra el archivo transferencias.log.
Puedes usar un visor de registros como tail para seguir en tiempo real los registros:

```shell
tail -f transferencias.log
```

Esto mostrará los registros en tiempo real mientras la aplicación esté en funcionamiento.

También puedes abrir el archivo transferencias.log con un editor de texto para revisar los registros en 
cualquier momento.

# Arquitectura y Decisiones de Diseño

## Estructura del Proyecto

El proyecto sigue una estructura típica de Django, con la separación de la lógica de negocio en aplicaciones Django 
individuales. En este caso, tenemos la aplicacion `transferencias_app` con su propio  conjunto de modelos, vistas, 
serializadores y servicios.

## Patrones de Diseño

   - Modelo-Vista-Servicio (MVS): Se implementó un patrón MVS para separar la lógica de negocio (servicios) de 
   las vistas y los modelos. Los servicios se encargan de manejar la lógica compleja y las interacciones con 
   la base de datos.

   - Inyección de Dependencias: Se utiliza la inyección de dependencias en TransferenciaService para permitir la 
   configuración flexible del modelo de Transferencia.

## Principios SOLID
   - Principio de Responsabilidad Única (SRP): Cada clase y método tiene una sola razón para cambiar y se enfoca en 
   hacer una sola cosa. Por ejemplo, ClienteService se encarga exclusivamente de la lógica relacionada con los 
   clientes.

   - Principio de Abierto/Cerrado (OCP): El código está diseñado para ser extendido fácilmente sin necesidad de 
   modificar el código existente. Por ejemplo, si se desea agregar más funcionalidades a TransferenciaService, 
   se puede hacer sin modificar el código existente.

   - Principio de Sustitución de Liskov (LSP): Las clases derivadas pueden ser sustituidas por sus clases base 
   sin afectar el comportamiento del programa. En este proyecto, las clases de servicio (ClienteService, 
   BeneficiarioService, TransferenciaService) pueden ser intercambiadas fácilmente sin afectar el funcionamiento 
   de las vistas.

## Decisiones de Diseño Adicionales
 
   - Manejo de Excepciones: Se implementa un manejo robusto de excepciones para manejar errores y excepciones de 
   manera adecuada.

   - Utilización de Transacciones: Se utilizan transacciones para garantizar la atomicidad de las operaciones de base 
   de datos, especialmente en los servicios de creación y actualización.

   - Separación de Responsabilidades: Se separa claramente la lógica de negocio de la lógica de presentación, 
   siguiendo el principio de separación de responsabilidades.
