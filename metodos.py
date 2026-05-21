from lista import lista
from contacto import contacto

def nuevo_contacto(lista_contactos):
    print("\n--- Registro de Nuevo Contacto ---")

    #Agregar los inputs de todos los campos

    nuevo_contacto = contacto()

    lista_contactos.insertar(nuevo_contacto)

    print("\n Contacto guardado con éxito.")
    input("Presiona Enter para continuar...")