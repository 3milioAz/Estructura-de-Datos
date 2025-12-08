class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        
        actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, "-> ", end="")
            actual = actual.siguiente
        print("None")


# PRUEBA
if __name__ == "__main__":
    lista = ListaEnlazadaSimple()

    lista.insertar_al_inicio(10)
    lista.insertar_al_inicio(20)

    lista.insertar_al_final(30)
    lista.insertar_al_final(40)

    lista.insertar_al_inicio(50)

    lista.imprimir_lista()
