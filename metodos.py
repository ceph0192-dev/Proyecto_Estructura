from lista import Lista
from contacto import Contacto
from datetime import datetime

def nuevo_contacto(mi_lista):
    while True:
        Nombres = input("Ingrese el nombre: ")

        if Nombres != "" and Nombres.replace(" ","").isalpha() and len(Nombres) < 80:
            break
        else:
            print("No puede estar vacío ni contener números.")

    while True:
        Paterno = input("Ingrese el apellido paterno: ")

        if Paterno != "" and Paterno.replace(" ","").isalpha() and len(Paterno) < 80:
            break
        else:
            print("No puede estar vacío ni contener números.")

    while True:
        Materno = input("Ingrese el apellido materno: ")

        if Materno != "" and Materno.replace(" ","").isalpha() and len(Materno) < 80:
            break
        else:
            print("No puede estar vacío ni contener números.")

    while True:
        Direccion = input("Ingrese la dirección: ")

        if Direccion != "" and len(Direccion) < 80:
            break
        else:
            print("No puede estar vacío")

    while True:
        Estado = input("Ingrese el estado: ")

        if Estado != "" and len(Estado) < 80:
            break
        else:
            print("No puede estar vacío")

    while True:
        Ciudad = input("Ingrese la ciudad: ")

        if Ciudad != "" and len(Ciudad) < 80:
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

        if Fac != "" and len(Fac) < 40:
            break
        else:
            print("No puede estar vacío")

    while True:
        Lic = input("Ingrese la licenciatura: ")

        if Lic != "" and len(Lic) < 80:
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
    
    if mi_lista.buscar_por_id(nuevo_contacto.get_id()) is not None: #verifica si ya existe un contacto con la misma matrícula antes de agregarlo
        print("Ya existe un contacto con esta matrícula. No se puede agregar.")
        input("Presiona Enter para continuar...")
        return
    
    mi_lista.insertar(nuevo_contacto)
    print("\n Contacto guardado con éxito.")
    input("Presiona Enter para continuar...")

def buscar_contacto(mi_lista):
    while True:
        matricula = input("Ingrese la matrícula del contacto a buscar: ")
        if matricula != "" and matricula.isalnum():
            break
        else:
            print("La matrícula no puede estar vacía")
        
    id_buscar = _calcular_id_matricula(matricula)
    nodo = mi_lista.buscar_por_id(id_buscar)

    if nodo is None or nodo.dato.get_Matricula() != matricula:
        print("No se encontró ningún contacto con esa matrícula.")
    else:
        print("\n Contacto encontrado:")
        nodo.dato.mostrar_info()

    input("Presiona Enter para continuar...")

def actualizar_contacto(mi_lista):
    while True:
        matricula = input("Ingrese la matrícula del contacto a actualizar: ")
        if matricula != "" and matricula.isalnum():
            break
        else:
            print("La matrícula no puede estar vacía")
        
    id_buscar = _calcular_id_matricula(matricula)
    nodo = mi_lista.buscar_por_id(id_buscar)

    if nodo is None or nodo.dato.get_Matricula() != matricula:
        print("No se encontró ningún contacto con esa matrícula.")
        input("Presiona Enter para continuar...")
        return
    
    temp = nodo.dato
    print(f"\n Contacto encontrado: {temp.get_nombre_completo()}")
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
        
    mi_lista.actualizar(matricula, actualizar_contacto)

    print( "\n Contacto actualizado")
    input("Presiona Enter para continuar...")

def eliminar_contacto(mi_lista): #Elimina un contacto de la lista por su matrícula
    while True:
        Matricula = input("Ingrese la matrícula del contacto a eliminar: ")
        if Matricula != "" and Matricula.isalnum():
            break
        else:
            print("La matrícula no puede estar vacía")
        
    id_buscar = _calcular_id_matricula(Matricula)
    nodo = mi_lista.buscar_por_id(id_buscar)

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
        mi_lista.eliminar(Matricula, id_buscar)
        print("Contacto eliminado.")
    else:
        print("\n Operación cancelada")
    input("Presiona Enter para continuar...")

# ----------------------------------
# REPORTE DE CONTACTOS
# ----------------------------------

def _contacto_txt(contacto):
    separador = "-" * 40

    if contacto.get_T_actualizacion():
        # Corregido: Llamamos al método correcto get_T_actualizacion()
        actualizacion = contacto.get_T_actualizacion().strftime('%d/%m/%Y %H:%M:%S')
    else:
        actualizacion = "No se ha actualizado aún" 
    
    # Corregido: Se agregaron las comas al final de cada línea
    # Corregido: Se eliminaron los \n manuales, el método .join() ya los pone
    datos = [
        separador,
        f"ID: {contacto.get_id()}",
        f"Nombre Completo: {contacto.get_nombre_completo()}",
        f"Dirección: {contacto.get_Direccion()}",
        f"Estado: {contacto.get_Estado()}",
        f"Ciudad: {contacto.get_Ciudad()}",
        f"Fecha de Nacimiento: {contacto.get_Nacimiento().strftime('%d/%m/%Y')}",
        f"Teléfono: {contacto.get_Tel()}",
        f"Correo Personal: {contacto.get_C_personal()}",
        f"Matrícula: {contacto.get_Matricula()}",
        f"Correo Institucional: {contacto.get_C_institucional()}",
        f"Facultad: {contacto.get_Fac()}",
        f"Licenciatura: {contacto.get_Lic()}",
        f"Fecha de Ingreso: {contacto.get_F_ingreso().strftime('%d/%m/%Y')}",
        f"Fecha de Registro: {contacto.get_F_registro().strftime('%d/%m/%Y')}",
        f"Fecha de Última Actualización: {actualizacion}", 
        separador,
    ]
    return "\n".join(datos)

def _cabecera_reporte(titulo, detalle):
    separador = "=" * 50
    
    datos = [
        separador,
        titulo, 
        separador,
        detalle,
        datetime.now().strftime('%d/%m/%Y %H:%M:%S'), #fecha de creación del reporte
        separador,
    ]

    return "\n".join(datos)

def _guardar_reporte(nombre_archivo, contenido):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print(f"\n Reporte guardado como '{nombre_archivo}'")

def reporte_matricula(mi_lista):
    while True:
        matricula = input("Ingrese la matrícula del contacto para generar el reporte: ")
        if matricula != "" and matricula.isalnum():
            break
        else:
            print("La matrícula no puede estar vacía")
        
    id_buscar = _calcular_id_matricula(matricula)
    nodo = mi_lista.buscar_por_id(id_buscar)

    if nodo is None or nodo.dato.get_Matricula() != matricula:
        print("No se encontró ningún contacto con esa matrícula.")
        input("Presiona Enter para continuar...")
        return
    
    contacto = nodo.dato
    titulo = f"Reporte de Contacto - {contacto.get_nombre_completo()}"
    detalle = f"Matrícula: {contacto.get_Matricula()}"
    
    contenido_reporte = _cabecera_reporte(titulo, detalle) + "\n\n" + _contacto_txt(contacto)
    
    nombre_archivo = f"reporte_{contacto.get_Matricula()}.txt"
    _guardar_reporte(nombre_archivo, contenido_reporte)
    
    input("Presiona Enter para continuar...")

def reporte_fechas(mi_lista):
    while True:
        fecha_inicio_str = input("Ingrese la fecha de inicio (DD/MM/AAAA): ")
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Formato incorrecto. Usa el formato DD/MM/AAAA")

    while True:
        fecha_fin_str = input("Ingrese la fecha de fin (DD/MM/AAAA): ")
        try:
            fecha_fin = datetime.strptime(fecha_fin_str, "%d/%m/%Y").date()
            if fecha_fin >= fecha_inicio:
                break
            else:
                print("La fecha de fin debe ser igual o posterior a la fecha de inicio.")
        except ValueError:
            print("Formato incorrecto. Usa el formato DD/MM/AAAA")

    contactos_filtrados = mi_lista.filtrar_por_fecha_ingreso(fecha_inicio, fecha_fin) #posible error

    if not contactos_filtrados:
        print("No se encontraron contactos con fechas de ingreso dentro del rango especificado.")
        input("Presiona Enter para continuar...")
        return

    titulo = f"Reporte de Contactos por Fecha de Ingreso"
    detalle = f"Rango: {fecha_inicio.strftime('%d/%m/%Y')} - {fecha_fin.strftime('%d/%m/%Y')}"
    
    contenido_reporte = _cabecera_reporte(titulo, detalle) + "\n\n"
    for contacto in contactos_filtrados:
        contenido_reporte += _contacto_txt(contacto) + "\n\n"

    nombre_archivo = f"reporte_fechas_{fecha_inicio.strftime('%Y%m%d')}_{fecha_fin.strftime('%Y%m%d')}.txt"
    _guardar_reporte(nombre_archivo, contenido_reporte)
    
    input("Presiona Enter para continuar...")

#Codigi reutilizable para calcular el ID a partir de la matrícula, asegurando que el mismo contacto siempre tenga el mismo ID incluso si se actualiza su información
def _calcular_id_matricula(matricula):
    valor_hash = 0
    primo = 31
    for caracter in matricula:
        valor_hash = (valor_hash * primo) + ord(caracter)
    return str(valor_hash % 100000000).zfill(8)

def total_contactos(mi_lista):
    return mi_lista.tamaño()