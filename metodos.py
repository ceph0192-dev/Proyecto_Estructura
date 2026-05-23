from lista import Lista
from contacto import contacto
from datetime import datetime

def nuevo_contacto(lista_contactos):
    while True:
        Nombres = input("Ingrese el nombre: ")

        if Nombres != "" and Nombres.replace(" ","").isalpha() and len(Nombres) < 2254:
            break
        else:
            print("No puede estar vacío ni contener números.")

    while True:
        Paterno = input("Ingrese el apellido paterno: ")

        if Paterno != "" and Nombres.replace(" ","").isalpha():
            break
        else:
            print("No puede estar vacío ni contener números.")

    while True:
        Materno = input("Ingrese el apellido materno: ")

        if Materno != "" and Nombres.replace(" ","").isalpha():
            break
        else:
            print("No puede estar vacío ni contener números.")

    while True:
        Direccion = input("Ingrese la dirección: ")

        if Direccion != "":
            break
        else:
            print("No puede estar vacío")

    while True:
        Estado = input("Ingrese el estado: ")

        if Estado != "":
            break
        else:
            print("No puede estar vacío")

    while True:
        Ciudad = input("Ingrese la ciudad: ")

        if Ciudad != "":
            break
        else:
            print("No puede estar vacío")

    while True:
        Nac_str = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")

        try:
            Nacimiento = datetime.strptime(Nac_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Formato incorrecto. Usa el formato DD/MM/AAAA")

    while True:
        Tel = input("Ingrese el numero de telefono: ")
        
        if Tel.isdigit() and len(Tel) == 10:
            break
        else:
            print("El teléfono debe contener exactamente 10 números.")

    while True:
        C_personal = input("Ingrese el correo personal: ")
        if C_personal != "":
            break
        else:
            print("No puede estar vacío")

    while True:
        Matricula = input("Ingrese la matricula: ")

        if Matricula != "":
            break
        else:
            print("No puede estar vacío")

    while True:
        C_institucional = input("Ingrese el correo institucional: ")

        if C_institucional != "":
            break
        else:
            print("No puede estar vacío")

    while True:
        Fac = input("Ingrese la facultad: ")

        if Fac != "":
            break
        else:
            print("No puede estar vacío")

    while True:
        Lic = input("Ingrese la licenciatura: ")

        if Lic != "":
            break
        else:
            print("No puede estar vacío")

    while True:
        F_ingreso_str = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ")

        try:
            F_ingreso = datetime.strptime(F_ingreso_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Formato incorrecto. Usa el formato DD/MM/AAAA")

    Nacimiento = datetime.strptime(Nac_str, "%d/%m/%Y").date()
    F_ingreso = datetime.strptime(F_ingreso_str, "%d/%m/%Y").date()


    nuevo_contacto = contacto(Nombres, Paterno, Materno, Direccion, Estado, Ciudad, 
                    Nacimiento, Tel, C_personal, Matricula,
                    C_institucional, Fac, Lic, F_ingreso)

    lista_contactos.insertar(nuevo_contacto)

    print("\nContacto guardado con éxito.")
    input("Presiona Enter para continuar...")