from datetime import datetime
class contacto:
    def __init__(self, id, Nombres, Paterno, Materno,
Direccion, Estado, Ciudad, Nacimiento, Edad, Tel, C_personal, 
Matricula, C_institucional, Fac, Lic, F_ingreso,
Antiguedad, F_registro, T_actualizacion):
        self.__id = None
        self.__Nombres = Nombres
        self.__Paterno = Paterno
        self.__Materno = Materno
        self.__Direccion = Direccion
        self.__Estado = Estado
        self.__Ciudad = Ciudad
        self.__Nacimiento = Nacimiento
        self.__Edad = None
        self.__Tel = Tel
        self.__C_personal = C_personal
        self.__Matricula = Matricula
        self.__C_institucional = C_institucional
        self.__Fac = Fac
        self.__Lic = Lic
        self.__F_ingreso = F_ingreso
        self.__Antiguedad = None
        self.__F_registro = None
        self.__T_actualizacion = T_actualizacion
