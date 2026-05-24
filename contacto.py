from datetime import date, datetime

class contacto:
    def __init__(self, Nombres, Paterno, Materno,
                Direccion, Estado, Ciudad, Nacimiento, Tel, C_personal, 
                Matricula, C_institucional, Fac, Lic, F_ingreso):

        self.__Matricula = Matricula
        self.__id = self.calcular_id()#Genera el id a partir de un metodo propio tipo hash
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
        self.__C_institucional = C_institucional
        self.__Fac = Fac
        self.__Lic = Lic
        self.__F_ingreso = F_ingreso # Fecha almacenada como objeto date
        self.__Antiguedad = self.__calcular_antiguedad() # Calcula la antigüedad a partir de la fecha de ingreso
        self.__F_registro = date.today() # Lo toma automaticamente del sistema 
        self.__T_actualizacion = None # Se actualiza cada vez que se modifica el contacto

    def calcular_id(self):
        prox_id = self.__Matricula
        valor_hash = 0
        primo = 31
        
        for caracter in prox_id:
            valor_hash = (valor_hash * primo) + ord(caracter)

        id = valor_hash % 100000000

        return str(id).zfill(8)

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

    # Getters para acceder a los atributos privados del contacto
    def get_id(self):
        return self.__id

    def get_Nombres(self):
        return self.__Nombres

    def get_Paterno(self):
        return self.__Paterno

    def get_Materno(self):
        return self.__Materno

    def get_nombre_completo(self):
        return f"{self.__Nombres} {self.__Paterno} {self.__Materno}"

    def get_Direccion(self):
        return self.__Direccion

    def get_Estado(self):
        return self.__Estado

    def get_Ciudad(self):
        return self.__Ciudad

    def get_Nacimiento(self):
        return self.__Nacimiento

    def get_Edad(self): # Recalcula la edad siempre para qur sea precisa
        return self.__calcular_edad()

    def get_Tel(self):
        return self.__Tel

    def get_C_personal(self):
        return self.__C_personal

    def get_Matricula(self):
        return self.__Matricula

    def get_C_institucional(self):
        return self.__C_institucional

    def get_Fac(self):
        return self.__Fac

    def get_Lic(self):
        return self.__Lic

    def get_F_ingreso(self):
        return self.__F_ingreso

    def get_Antiguedad(self): # Recalcula la antigüedad siempre para que sea precisa
        return self.__calcular_antiguedad()

    def get_F_registro(self):
        return self.__F_registro

    def get_T_actualizacion(self):
        return self.__T_actualizacion

    # Setters para modificar los atributos del contacto
    def set_Nombres(self, valor):
        self.__Nombres = valor 

    def set_Paterno(self, valor):
        self.__Paterno = valor

    def set_Materno(self, valor):
        self.__Materno = valor

    def set_Direccion(self, valor):
        self.__Direccion = valor

    def set_Estado(self, valor):
        self.__Estado = valor

    def set_Ciudad(self, valor):
        self.__Ciudad = valor

    def set_Nacimiento(self, valor):
        self.__Nacimiento = valor
        self.__Edad = self.__calcular_edad() # Actualiza la edad automáticamente

    def set_Tel(self, valor):
        self.__Tel = valor

    def set_C_personal(self, valor):
        self.__C_personal = valor

    def set_Matricula(self, valor):
        self.__Matricula = valor

    def set_C_institucional(self, valor):
        self.__C_institucional = valor

    def set_Fac(self, valor):
        self.__Fac = valor

    def set_Lic(self, valor):
        self.__Lic = valor

    def set_F_ingreso(self, valor):
        self.__F_ingreso = valor
        self.__Antiguedad = self.__calcular_antiguedad() 

    def marcar_actualizacion(self):
        self.__T_actualizacion = datetime.now() # Registra la fecha y hora de la última actualización 

    def mostrar_info(self):

        print("ID:", self.get_id())

      print("ID:", self.get_id())
      print("Nombre Completo:", self.get_nombre_completo())
