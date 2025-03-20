from libro import Libro

class Bibliteca:
    # Constructor de la clase
    def __init__(self):
        # Creamos una lista vacía para guardar los libros.
        self.libros = []
    
    # Método de agregar libro a la biblioteca
    def agregar_libros(self, titulo, autor, anio, genero):
        # Creamos un nuevo objeto de tipo Libro
        libro = Libro(titulo, autor, anio, genero)
        self.libros.append(libro)  # Agregamos el objeto libro a la lista
        # Mensaje de confirmación.
        print(f"\nLibro '{titulo}' agregado correctamente\n")
    
    # Método mostrar todos los libros de la biblioteca
    def listar_libros(self):
        if not self.libros:
            print("\nNo existen libros en la Biblioteca.\n")
            return
        # Si existen libros, los mostramos con un índice
        print("\nLista de Libros:\n")
        for i, libro in enumerate(self.libros, start=1):
            print(f"{i}. {libro}")  # Llamamos automáticamente al método __str__ del libro
            print()
    
    # Método para buscar libros por título o autor
    def buscar_libros(self, criterio):
        # Filtramos los libros que coinciden con los criterios sin importar mayúsculas o minúsculas
        resultados = [
            libro for libro in self.libros 
            if criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor.lower()
        ]
        if resultados:
            print("\nResultados de Búsqueda:")
            for libro in resultados:
                print(f"- {libro}")
        else:
            print("\nNo se encuentran libros con estos criterios.\n")

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():  # Comparar con el título del libro
                self.libros.remove(libro)  # Eliminamos libro de la lista
                print(f"\nLibro '{titulo}' eliminado correctamente.")
                return
        print(f"\nNo encontramos el libro '{titulo}'.\n")  # Fuera del bucle

    def guardar_datos(self, archivo):
        with open(archivo, "w") as f:  # Cambiado a modo escritura
            for libro in self.libros:
                f.write(f"{libro.titulo}, {libro.autor}, {libro.anio}, {libro.genero}\n")
        print(f"\nDatos guardados en '{archivo}'.\n")

    # Método para cargar los datos desde el archivo
    def cargar_datos(self, archivo):
        try:
            with open(archivo, "r") as f:
                for linea in f:
                    # Dividimos las líneas por comas para obtener los datos del libro
                    titulo, autor, anio, genero = linea.strip().split(',')
                    self.agregar_libros(titulo, autor, anio, genero)
            print(f"\nDatos cargados desde '{archivo}'.\n")
        except FileNotFoundError:
            print(f"\nEl archivo '{archivo}' no existe.\n")