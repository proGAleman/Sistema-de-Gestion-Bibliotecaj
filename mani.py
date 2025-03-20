from biblioteca import Bibliteca
print()
# Funcion para mostrar menu de opciones
def mostrar_menu():

    print("Sistema de Gestion de Bliblioteca")
    print("\n-----MENU-----\n")
    print("1. Agregar Libro")
    print("2. Listar Libros")
    print("3. Buscar Libros")
    print("4. Eliminar Libro")
    print("5. Guarda Libro")
    print("6. Cargar Datos")
    print("7. Salir")
# Funcion Principal
def main():
    # Intancia de la Bibioteca.
    biblioteca = Bibliteca()

    while True:
        mostrar_menu()
        opcion = input ("Seleccione una Opcion: ")
        if opcion =="1":
            titulo = input("Titulo : ") 
            autor = input("Autor: ")
            anio = input("año: ")
            genero = input("Genero: ")
            biblioteca.agregar_libros(titulo, autor, anio, genero)
        
        elif opcion =="2":
            biblioteca.listar_libros()
        
        elif opcion =="3":
            criterio = input("Buscar por titulo o autor: ")
            biblioteca.buscar_libros(criterio)

        elif opcion =="4":
            titulo = input("Titulo del libro a eliminar: ")
            biblioteca.eliminar_libro(titulo)
        
        elif opcion =="5":
            archivo = input("Nombre del archivo para guardar datos: ")
            biblioteca.guardar_datos(archivo)

        elif opcion =="6":
            archivo = input("Nombre de archivo para cargar datos: ")
            biblioteca.cargar_datos(archivo)

        elif opcion =="7":
            print("\n!Hasta luego\n")
            break

        else:
            print("\nOpcion Selecionada, no valida: ")
            
# si ejecutamo directamente llama a la funcion Main()
if __name__=="__main__":
    main()




