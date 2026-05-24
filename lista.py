from nodo import Nodo

class Lista:
    def __init__(self):
        self.__head = None
        self.__tamaño = 0
    
    def insertar(self,contacto):
        nuevo_nodo = Nodo(contacto)

        if self.__head is None:
            self.__head = nuevo_nodo
        
        else:
            temp = self.__head
            while temp.siguiente:
                temp = temp.siguiente
            
            temp.siguiente = nuevo_nodo