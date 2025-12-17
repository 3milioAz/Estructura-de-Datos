class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # Agregar un nodo al final de la lista
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            return

        self.cola.siguiente = nuevo_nodo
        nuevo_nodo.anterior = self.cola
        self.cola = nuevo_nodo

    def imprimir_hacia_adelante(self):
        actual = self.cabeza
        while actual is not None:
            print(f"{actual.dato} <-> ", end="")
            actual = actual.siguiente
        print("None")

    def imprimir_hacia_atras(self):
        actual = self.cola
        while actual is not None:
            print(f"{actual.dato} <-> ", end="")
            actual = actual.anterior
        print("None")


# Programa principal (equivalente al main en Java)
if __name__ == "__main__":
    lista = ListaDoble()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.agregar(4)

    print("Recorremos hacia adelante:")
    lista.imprimir_hacia_adelante()

    print("Recorremos hacia atrás:")
    lista.imprimir_hacia_atras()