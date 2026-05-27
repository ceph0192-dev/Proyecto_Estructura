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

def menu_reportes():
    print("\n" + "="*20)
    print("   MENÚ REPORTES  ")
    print("="*20)
    print("1. Generar reporte por matrículas")
    print("2. Generar reporte por fecha de registro")
    print("3. Regresar al menú principal")
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
            os.system('clear' if os.name == 'posix' else 'cls')
            metodos.buscar_contacto(mi_lista)

        elif opcion == "3":
            os.system('clear' if os.name == 'posix' else 'cls')
            metodos.actualizar_contacto(mi_lista)

        elif opcion== "4":
            os.system('clear' if os.name == 'posix' else 'cls')
            metodos.eliminar_contacto(mi_lista)

        elif opcion == "5":
            while True:
                os.system('clear' if os.name == 'posix' else 'cls')

                menu_reportes()

                if error != "":
                    print(error)
                error = ""

                opcion = input("Elige una opción (1-3): ")

                if opcion == "1":
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print("\n" + "="*20)
                    print("   Reporte por matrícula   ")
                    print("="*20)
                    metodos.reporte_matricula(mi_lista)

                elif opcion == "2":
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print("\n" + "="*20)
                    print("   Reporte por fechas  ")
                    print("="*20)
                    metodos.reporte_fechas(mi_lista)

                elif opcion == "3":
                    break

                else:
                    error = "Opcion no válida. Elige una opción correcta"



        elif opcion == "6":
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Finalización del programa. Adioooooooooooooooooooooos..........")
            break

        else:
            error = "Opcion no válida. Elige una opción correcta"