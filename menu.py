#Bliblioteca esatandar de python
import os

#Modulos propios del proyecto
import metodos
from lista import Lista

def menu():
    print("\n" + "="*20)
    print("   MENÚ PRINCIPAL   ")
    print("="*20)
    print("1. Registrar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Generar reporte")
    print("6. Salir del programa")
    print("="*20)

def mostrar_menu():
    error = ""

    mi_lista = Lista()

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
            
        menu()

        if error != "":
            print(error)
            error = ""

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            os.system('clear' if os.name == 'posix' else 'cls')
            print("\n" + "="*20)
            print("   Registrar contacto   ")
            print("="*20)
            metodos.nuevo_contacto(mi_lista)

        elif opcion == "2":
            pass

        elif opcion == "3":
            pass

        elif opcion== "4":
            pass

        elif opcion == "5":
            pass

        elif opcion == "6":
            break

        else:
            error = "Opcion no válida. Elige una opción correcta"