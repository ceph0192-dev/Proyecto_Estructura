from nodo import Nodo

class Lista:
    def __init__(self):
        self.__head = None
        self.__tamaño = 0
    
    def insertar(self,contacto): #INsertar al final de la lista
        nuevo_nodo = Nodo(contacto)

        if self.__head is None:
            self.__head = nuevo_nodo
        
        else:
            temp = self.__head
            while temp.siguiente is not None:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
        self.__tamaño += 1
        return nuevo_nodo
    
    def buscar(self, matricula): #Busca un contacto por su matrícula y devuelve el nodo que lo contiene
        temp = self.__head
        while temp is not None:
            if temp.dato.get_Matricula() == matricula:
                return temp
            temp = temp.siguiente
        return None
    
    def actualizar(self, matricula, nuevo_contacto): #Actualiza un contacto existente con nueva información
        nodo_a_actualizar = self.buscar(matricula)
        if nodo_a_actualizar is not None:
            nodo_a_actualizar.dato = nuevo_contacto
            return True
        return False
    
    def eliminar(self, matricula): #Elimina un contacto de la lista por su matrícula
        if self.__head is None:
            return False
        
        if self.__head.dato.get_Matricula() == matricula: #Si el contacto a eliminar es el primero de la lista
            self.__head = self.__head.siguiente
            self.__tamaño -= 1
            return True
        
        anterior = self.__head
        temp = self.__head.siguiente
        while temp is not None:
            if temp.dato.get_Matricula() == matricula:
                anterior.siguiente = temp.siguiente
                self.__tamaño -= 1
                return True
            anterior = temp
            temp = temp.siguiente
        return False
    
    def está_vacía(self): #Verifica si la lista está vacía
        return self.__head is None
    
    def tamaño(self): #Devuelve el número de contactos en la lista
        return self.__tamaño
    
    def mostrar_todos(self): #Muestra la información de todos los contactos en la lista
        resultado = []
        temp = self.__head
        while temp is not None:
            resultado.append(temp.dato)
            temp = temp.siguiente
        return resultado