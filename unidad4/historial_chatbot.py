class Nodo:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.siguiente = None

class HistorialChat:
    def __init__(self):
        self.inicio = None

    def agregar_mensaje(self, mensaje):
        nuevo = Nodo(mensaje)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar_historial(self):
        actual = self.inicio
        while actual:
            print(actual.mensaje)
            actual = actual.siguiente

chat = HistorialChat()
chat.agregar_mensaje("Hola")
chat.agregar_mensaje("¿En qué puedo ayudarte?")
chat.mostrar_historial()