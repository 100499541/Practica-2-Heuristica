# Módulo de Python para usar heaps (colas de prioridad)
import heapq

# Definimos la clase Abierta, que representa la lista abierta para A* o Dijkstra
class Abierta:

    def __init__(self):
        # Inicializamos un heap vacío; aquí se guardarán las tuplas (coste_total, nodo, path)
        # El heap nos permite extraer siempre el nodo con menor coste_total eficientemente
        self.heap = []

    # Método para añadir un nodo al heap
    def push(self, coste_total, nodo, path):
        # Añadimos una tupla (coste_total, nodo, path) al heap
        # heapq asegura que el heap se mantiene ordenado por coste_total automáticamente
        heapq.heappush(self.heap, (coste_total, nodo, path))

    # Método para extraer el nodo con menor coste_total
    def pop(self):
        # Elimina y devuelve la tupla con menor coste_total del heap
        return heapq.heappop(self.heap)

    # Método para comprobar si el heap está vacío
    def vacia(self):
        # Devuelve True si no hay nodos en la lista abierta, False en caso contrario
        return len(self.heap) == 0
