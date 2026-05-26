from lista import Lista
from contacto import Contacto
from datetime import datetime

lista_contactos = Lista()

def nuevo_contacto():
    while True:
        Nombres = input("Ingrese el nombre: ")

        if Nombres != "" and Nombres.replace(" ","").isalpha() and len(Nombres) < 80:
            break
        else:
            print("No puede estar vacío ni contener números.")

    while True:
        Paterno = input("Ingrese el apellido paterno: ")

        if Paterno != "" and Paterno.replace(" ","").isalpha():
            break
        else:
            print("No puede estar vacío ni contener números.")

    while True:
        Materno = input("Ingrese el apellido materno: ")

        if Materno != "" and Materno.replace(" ","").isalpha():
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
        if C_personal != "" and "@" in C_personal and "." in C_personal:
            break
        else:
            print("No puede estar vacío")

    while True:
        Matricula = input("Ingrese la matricula: ")

        if Matricula != "" and Matricula.isalnum() and len(Matricula) < 20:
            break
        else:
            print("No puede estar vacío")

    while True:
        C_institucional = input("Ingrese el correo institucional: ")

        if C_institucional != "" and "@" in C_institucional and "." in C_institucional:
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

    nuevo_contacto = Contacto(Nombres=Nombres, Paterno=Paterno, Materno=Materno, Direccion=Direccion, Estado=Estado, Ciudad=Ciudad,
                    Nacimiento=Nacimiento, Tel=Tel, C_personal=C_personal, Matricula=Matricula,
                    C_institucional=C_institucional, Fac=Fac, Lic=Lic, F_ingreso=F_ingreso)

    if lista_contactos.existe_id(nuevo_contacto.get_id()): #verifica si ya existe un contacto con la misma matrícula antes de agregarlo
        print("Ya existe un contacto con esta matrícula. No se puede agregar.")
        input("Presiona Enter para continuar...")
        return
    
    lista_contactos.agregar(nuevo_contacto)
    print("\n Contacto guardado con éxito.")
    input("Presiona Enter para continuar...")

    def buscar_contacto():
        while True:
            matricula = input("Ingrese la matrícula del contacto a buscar: ")
            if matricula != "" and matricula.isalnum():
                break
            else:
                print("La matrícula no puede estar vacía")
        
        id_buscar = _calcular_id_matricula(matricula)
        nodo = lista_contactos.buscar_por_id(id_buscar)

        if nodo is None or nodo.dato.get_Matricula() != matricula:
            print("No se encontró ningún contacto con esa matrícula.")
        else:
            print("\n Contacto encontrado:")
            nodo.dato.mostrar_info()

        input("Presiona Enter para continuar...")

    def actualizar_contacto():
        while True:
            matricula = input("Ingrese la matrícula del contacto a actualizar: ")
            if matricula != "" and matricula.isalnum():
                break
            else:
                print("La matrícula no puede estar vacía")
        
        id_buscar = _calcular_id_matricula(matricula)
        nodo = lista_contactos.buscar_por_id(id_buscar)

        if nodo is None or nodo.dato.get_Matricula() != matricula:
            print("No se encontró ningún contacto con esa matrícula.")
            input("Presiona Enter para continuar...")
            return
        
        temp = nodo.dato
        print("\n Contacto encontrado: {temp.get_nombre_completo()}")
        print("Ingrese la nueva información (deja en blanco para mantener el valor actual):")

        while True: #Nombres
            nuevo_nombre = input(f"Nombre(s) ({temp.get_Nombres()}): ")
            if nuevo_nombre == "":
                nuevo_nombre = temp.get_Nombres()
                break
            elif nuevo_nombre.replace(" ","").isalpha():
                break
            else:
                print("No puede contener números.")
        
        while True: #Paterno
            nuevo_paterno = input(f"Apellido Paterno ({temp.get_Paterno()}): ")
            if nuevo_paterno == "":
                nuevo_paterno = temp.get_Paterno()
                break
            elif nuevo_paterno.replace(" ","").isalpha():
                break
            else:
                print("No puede contener números.")
        
        while True: #Materno
            nuevo_materno = input(f"Apellido Materno ({temp.get_Materno()}): ")
            if nuevo_materno == "":
                nuevo_materno = temp.get_Materno()
                break
            elif nuevo_materno.replace(" ","").isalpha():
                break
            else:
                print("No puede contener números.")
        
        nueva_direccion = input(f"Dirección ({temp.get_Direccion()}): ") #Direccion
        if nueva_direccion == "":
            nueva_direccion = temp.get_Direccion()

        nuevo_estado = input(f"Estado ({temp.get_Estado()}): ") #Estado
        if nuevo_estado == "":
            nuevo_estado = temp.get_Estado()

        nueva_ciudad = input(f"Ciudad ({temp.get_Ciudad()}): ") #Ciudad
        if nueva_ciudad == "":
            nueva_ciudad = temp.get_Ciudad()

        while True: #Nacimiento
            nuevo_nac_str = input(f"Fecha de Nacimiento ({temp.get_Nacimiento().strftime('%d/%m/%Y')}) (DD/MM/AAAA): ")
            if nuevo_nac_str == "":
                nuevo_nacimiento = temp.get_Nacimiento()
                break
            try:
                nuevo_nacimiento = datetime.strptime(nuevo_nac_str, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Formato incorrecto. Usa el formato DD/MM/AAAA")

        while True: #Telefono
            nuevo_tel = input(f"Teléfono ({temp.get_Tel()}): ")
            if nuevo_tel == "":
                nuevo_tel = temp.get_Tel()
                break
            elif nuevo_tel.isdigit() and len(nuevo_tel) == 10:
                break
            else:
                print("El teléfono debe contener exactamente 10 números.")

        while True: #Correo Personal
            nuevo_c_personal = input(f"Correo Personal ({temp.get_C_personal()}): ")
            if nuevo_c_personal == "":
                nuevo_c_personal = temp.get_C_personal()
                break
            elif "@" in nuevo_c_personal and "." in nuevo_c_personal:
                break
            else:
                print("Ingresa un correo válido")

        while True: #Correo Institucional
            nuevo_c_institucional = input(f"Correo Institucional ({temp.get_C_institucional()}): ")
            if nuevo_c_institucional == "":
                nuevo_c_institucional = temp.get_C_institucional()
                break
            elif "@" in nuevo_c_institucional and "." in nuevo_c_institucional:
                break
            else:
                print("Ingresa un correo válido")

        nueva_fac = input(f"Facultad ({temp.get_Fac()}): ") #Facultad
        if nueva_fac == "":
            nueva_fac = temp.get_Fac()

        nueva_lic = input(f"Licenciatura ({temp.get_Lic()}): ") #Licenciatura
        if nueva_lic == "":
            nueva_lic = temp.get_Lic()
        
        while True: #Fecha de Ingreso
            nuevo_f_ingreso_str = input(f"Fecha de Ingreso ({temp.get_F_ingreso().strftime('%d/%m/%Y')}) (DD/MM/AAAA): ")
            if nuevo_f_ingreso_str == "":
                nuevo_f_ingreso = temp.get_F_ingreso()
                break
            try:
                nuevo_f_ingreso = datetime.strptime(nuevo_f_ingreso_str, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Formato incorrecto. Usa el formato DD/MM/AAAA")
        
        actualizar_contacto = Contacto(Nombres=nuevo_nombre, Paterno=nuevo_paterno, Materno=nuevo_materno, Direccion=nueva_direccion, Estado=nuevo_estado, Ciudad=nueva_ciudad,
                    Nacimiento=nuevo_nacimiento, Tel=nuevo_tel, C_personal=nuevo_c_personal, Matricula=matricula,
                    C_institucional=nuevo_c_institucional, Fac=nueva_fac, Lic=nueva_lic, F_ingreso=nuevo_f_ingreso)

        actualizar_contacto._Contacto__F_registro = temp.get_F_registro() # Mantiene la fecha de registro original
        actualizar_contacto.marcar_actualizacion() # Actualiza la fecha de última actualización
        
        lista_contactos.actualizar(matricula, actualizar_contacto)

        print( "\n Contacto actualizado")
        input("Presiona Enter para continuar...")

    def eliminar_contacto(): #Elimina un contacto de la lista por su matrícula
        while True:
            Matricula = input("Ingrese la matrícula del contacto a eliminar: ")
            if Matricula != "" and Matricula.isalnum():
                break
            else:
                print("La matrícula no puede estar vacía")
        
        id_buscar = _calcular_id_matricula(Matricula)
        nodo = lista_contactos.buscar_por_id(id_buscar)

        if nodo is None or nodo.dato.get_Matricula() != Matricula:
            print("No se encontró ningún contacto con esa matrícula.")
            input("Presiona Enter para continuar...")
            return
        
        while True:
            confirmar = input(f"Estas seguro de eliminar el contacto con la matricula {Matricula}? (S/N): ").upper()
            if confirmar in ("S", "N"):
                break
            else:
                print("Por favor ingresa 'S' para sí o 'N' para no.")

        if confirmar == "S":
            lista_contactos.eliminar(Matricula, id_buscar)
            print("Contacto eliminado.")
        else:
            print("\n Operación cancelada")
        input("Presiona Enter para continuar...")

# ----------------------------------
# REPORTE DE CONTACTOS
# ----------------------------------




def _calcular_id_matricula(matricula):
    valor_hash = 0
    primo = 31
    for caracter in matricula:
        valor_hash = (valor_hash * primo) + ord(caracter)
    return str(valor_hash % 1000000).zfill(8)
