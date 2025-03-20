# Sistema de Gestión de Biblioteca

## Descripción
Este proyecto es un sistema de gestión de biblioteca que permite a los usuarios agregar, listar, buscar, eliminar libros y guardar/cargar datos desde archivos. Está implementado en Python y utiliza una interfaz de línea de comandos para interactuar con el usuario.

## Estructura del Proyecto
- `biblioteca.py`: Contiene la clase `Bibliteca`, que gestiona la colección de libros.
- `libro.py`: Define la clase `Libro`, que representa un libro individual con atributos como título, autor, año y género.
- `mani.py`: Proporciona la interfaz de usuario y el menú para interactuar con el sistema de gestión de biblioteca.

## Funcionalidades
- **Agregar Libro**: Permite al usuario agregar un nuevo libro a la biblioteca.
- **Listar Libros**: Muestra todos los libros disponibles en la biblioteca.
- **Buscar Libros**: Permite buscar libros por título o autor.
- **Eliminar Libro**: Elimina un libro de la biblioteca por su título.
- **Guardar Datos**: Guarda la lista de libros en un archivo.
- **Cargar Datos**: Carga libros desde un archivo a la biblioteca.

## Uso
1. Ejecuta el archivo `mani.py` para iniciar el sistema.
2. Sigue las instrucciones en el menú para realizar diferentes acciones.

## Requisitos
- Python 3.x
