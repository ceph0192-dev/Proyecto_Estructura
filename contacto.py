from datetime import date, datetime

class contacto:
    def __init__(self, id_contacto, Nombres, Paterno, Materno,
Direccion, Estado, Ciudad, Nacimiento, Edad, Tel, C_personal, 
Matricula, C_institucional, Fac, Lic, F_ingreso,
Antiguedad, F_registro, T_actualizacion):
        
        # Calcula mediante la funcion hash
        self.__id = id_contacto 
        self.__Nombres = Nombres
        self.__Paterno = Paterno
        self.__Materno = Materno
        self.__Direccion = Direccion
        self.__Estado = Estado
        self.__Ciudad = Ciudad
        self.__Nacimiento = Nacimiento # Fecha almacenada como objeto date 
        self.__Edad = self.__calcular_edad() # Calcula la edad a partir de la fecha de nacimiento
        self.__Tel = Tel
        self.__C_personal = C_personal
        self.__Matricula = Matricula
        self.__C_institucional = C_institucional
        self.__Fac = Fac
        self.__Lic = Lic
        self.__F_ingreso = F_ingreso # Fecha almacenada como objeto date
        self.__Antiguedad = self.__calcular_antiguedad() # Calcula la antigüedad a partir de la fecha de ingreso
        self.__F_registro = date.today() # Lo toma automaticamente del sistema 
        self.__T_actualizacion = None # Se actualiza cada vez que se modifica el contacto

    def __calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.__Nacimiento.year 
        if (hoy.month, hoy.day) < (self.__Nacimiento.month, self.__Nacimiento.day):
            edad -= 1
        return edad
    
    def __calcular_antiguedad(self):
        hoy = date.today()
        años = hoy.year - self.__F_ingreso.year
        meses = hoy.month - self.__F_ingreso.month
        if meses < 0:
            años -= 1
            meses += 12
        return f"{años} años y {meses} meses"
    