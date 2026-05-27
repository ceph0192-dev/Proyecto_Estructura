from nodo import Nodo

class Lista:
    def __init__(self):
        self.__head = None
        self.__tamaño = 0
        self.__dic = {}
    
    def insertar(self,contacto): #Insertar al final de la lista
        nuevo_nodo = Nodo(contacto)

        if self.__head is None:
            self.__head = nuevo_nodo
        
        else:
            temp = self.__head
            while temp.siguiente is not None:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
        self.__tamaño += 1

        id_contacto = contacto.get_id()
        self.__dic[id_contacto] = nuevo_nodo

        return nuevo_nodo

    def buscar_por_id(self, id_contacto):#Busca la id del contacto en el dic y devuelve el nodo
        return self.__dic.get(id_contacto, None)

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
    
    def eliminar(self, matricula, id_contacto): #Elimina un contacto de la lista por su matrícula
        if self.__head is None:
            return False
        
        if self.__head.dato.get_Matricula() == matricula: #Si el contacto a eliminar es el primero de la lista
            self.__head = self.__head.siguiente
            self.__tamaño -= 1
            del self.__dic[id_contacto]
            return True
        
        anterior = self.__head
        temp = self.__head.siguiente
        while temp is not None:
            if temp.dato.get_Matricula() == matricula:
                anterior.siguiente = temp.siguiente
                self.__tamaño -= 1
                del self.__dic[id_contacto]
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

    def filtrar_por_fecha_ingreso(self, fecha_inicio, fecha_fin):
        resultados = []
        temp = self.__head
        while temp is not None:
            fecha_contacto = temp.dato.get_F_ingreso()
            if fecha_inicio <= fecha_contacto <= fecha_fin:
                resultados.append(temp.dato)
            temp = temp.siguiente
        return resultados