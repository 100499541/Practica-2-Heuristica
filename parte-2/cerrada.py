# Definimos la clase Cerrada, que representa la lista cerrada para A* o Dijkstra
class Cerrada:

    def __init__(self):
        # Inicializamos un conjunto vacío para guardar los nodos ya visitados
        self.visitados = set()

    # Método para añadir un nodo a la lista cerrada
    def add(self, nodo):
        # Añade el nodo al conjunto de visitados
        self.visitados.add(nodo)

    # Método para comprobar si un nodo ya ha sido visitado
    def contiene(self, nodo):
        # Devuelve True si el nodo ya está en la lista cerrada, False si no
        return nodo in self.visitados