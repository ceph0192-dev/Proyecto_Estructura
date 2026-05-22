from nodo import nodo
class Lista:
    def __init__(self):
        self.__head = None
    
    def insertar(self,dato):
        nuevo_nodo = nodo(dato)

        if self.__head is None:
            self.__head = nuevo_nodo
        
        else:
            temp = self.__head
            while temp.siguiente:
                temp = temp.siguiente
            
            temp.siguiente = nuevo_nodo