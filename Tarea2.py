class Nodo():
    def __init__(self):
        self.siguiente = None
        self.anterior = None
        self.contenido = None

class Lista():
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def insertar(self, dato):
        nuevo = Nodo()
        nuevo.contenido = dato
        if self.tamanio == 0:
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self.cabeza = nuevo
            self.tamanio = self.tamanio+1
        elif self.tamanio == 1:
            nuevo.siguiente = self.cabeza
            nuevo.anterior = self.cabeza
            self.cabeza.siguiente = nuevo
            self.cabeza.anterior = nuevo
            self.tamanio = self.tamanio+1
        else:
            aux = self.cabeza
            while aux.siguiente != self.cabeza:
                aux = aux.siguiente
            nuevo.siguiente = self.cabeza
            nuevo.anterior = aux
            aux.siguiente = nuevo
            self.cabeza.anterior = nuevo
            self.tamanio = self.tamanio + 1

    def mostrar(self):
        print("Lista completa:")
        aux = self.cabeza
        while aux.siguiente != self.cabeza:
            print("Dato:" + str(aux.contenido))
            aux = aux.siguiente
        print("Dato:" + str(aux.contenido))
        input()

    def seleccionar(self):
        dato = input("Seleccione numero: ")
        aux = self.cabeza
        while aux.siguiente != self.cabeza:
            if str(aux.contenido) == str(dato):
                print("Anterior: " + str(aux.anterior.contenido) + ", Actual: " + str(aux.contenido) + ", Siguiente: " + str(aux.siguiente.contenido))
                return
            else:
                aux = aux.siguiente
        if str(aux.contenido) == str(dato):
                print("Anterior: " + str(aux.anterior.contenido) + ", Actual: " + str(aux.contenido) + ", Siguiente: " + str(aux.siguiente.contenido))
                return

NuevaLista = Lista()
NuevaLista.insertar(5)
NuevaLista.insertar(9)
NuevaLista.insertar(7)
NuevaLista.insertar(27)
NuevaLista.insertar(14)
NuevaLista.mostrar()
NuevaLista.seleccionar()