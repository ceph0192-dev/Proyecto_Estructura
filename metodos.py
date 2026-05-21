from lista import lista
from contacto import contacto

def nuevo_contacto(lista_contactos):
    print("\n--- Registro de Nuevo Contacto ---")

    Nombres = input("Ingresa el nombre:")
    Paterno = input("Ingresa el apellido paterno:")
    Materno = input("Ingresa el apellido materno:")
    Direccion = input("Ingresa la dirección:")
    Estado = input("Ingresa el estado:")
    Ciudad = input("Ingresa la ciudad")
    ONacimient = input("Ingresa la frecha de nacimiento:")
    #Agregar los inputs de todos los campos

    nuevo_contacto = contacto()

    lista_contactos.insertar(nuevo_contacto)

    print("\n Contacto guardado con éxito.")
    input("Presiona Enter para continuar...")