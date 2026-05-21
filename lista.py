from nodo import nodo
class lista:
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
            
            temp = nuevo_nodo