# Class
class Libro:
    # metodo Costrutor de la clase ejecutamos automaticamente cuando creamos un nuevo objeto de la clase.
    def __init__(self, titulo, autor, anio, genero): 
       # Guardamos los datos que recibe costrutor como atras del objeto.
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self. genero = genero
    # Este metodo __str__ para definir como vamos haber el libro cuando imprimamos
    def __str__(self): 
        return f"{self.titulo} - {self.autor} - {self.anio} - {self.genero}"
    


    
