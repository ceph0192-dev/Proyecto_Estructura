from lista import Lista
from contacto import contacto
from datetime import datetime

def nuevo_contacto(lista_contactos):
    Nombres = input("Ingrese el nombre: ")
    Paterno = input("Ingrese el apellido paterno: ")
    Materno = input("Ingrese el apellido materno: ")
    Direccion = input("Ingrese la dirección: ")
    Estado = input("Ingrese el estado: ")
    Ciudad = input("Ingrese la ciudad: ")
    Nac_str = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
    Tel = input("Ingrese el numero de telefono: ")
    C_personal = input("Ingrese el correo personal: ")
    Matricula = input("Ingrese la matricula: ")
    C_institucional = input("Ingrese el correo institucional: ")
    Fac = input("Ingrese la facultad: ")
    Lic = input("Ingrese la licenciatura: ")
    F_ingreso_str = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ")

    Nacimiento = datetime.strptime(Nac_str, "%d/%m/%Y").date()
    F_ingreso = datetime.strptime(F_ingreso_str, "%d/%m/%Y").date()


    nuevo = contacto(Nombres, Paterno, Materno, Direccion, Estado, Ciudad, 
                    Nacimiento, Tel, C_personal, Matricula,
                    C_institucional, Fac, Lic, F_ingreso)

    lista_contactos.insertar(nuevo)

    print("\nContacto guardado con éxito.")
    input("Presiona Enter para continuar...")