# cerrada.py
class Cerrada:
    """Lista cerrada para marcar nodos ya visitados"""
    def __init__(self):
        self.visitados = set()

    def add(self, nodo):
        self.visitados.add(nodo)

    def contiene(self, nodo):
        return nodo in self.visitados