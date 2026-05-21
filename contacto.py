from datetime import datetime
class contacto:
    def __init__(self, id, Nombres, Paterno, Materno,
Direccion, Estado, Ciudad, Nacimiento, Edad, Tel, C_personal, 
Matricula, C_institucional, Fac, Lic, F_ingreso,
Antiguedad, F_registro, T_actualizacion):
        self.id = None
        self.Nombres = Nombres
        self.Paterno = Paterno
        self.Materno = Materno
        self.Direccion = Direccion
        self.Estado = Estado
        self.Ciudad = Ciudad
        self.Nacimiento = Nacimiento
        self.Edad = None
        self.Tel = Tel
        self.C_personal = C_personal
        self.Matricula = Matricula
        self.C_institucional = C_institucional
        self.Fac = Fac
        self.Lic = Lic
        self.F_ingreso = F_ingreso
        self.Antiguedad = None
        self.F_registro = None
        self.T_actualizacion = T_actualizacion
