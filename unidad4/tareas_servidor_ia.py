from collections import deque

cola = deque()

cola.append("Entrenar modelo A")
cola.append("Entrenar modelo B")

while cola:
    tarea = cola.popleft()
    print("Procesando:", tarea)