# abierta.py
import heapq

class Abierta:
    """Lista abierta para A* o Dijkstra usando heap"""
    def __init__(self):
        self.heap = []

    def push(self, coste_total, nodo, path):
        heapq.heappush(self.heap, (coste_total, nodo, path))

    def pop(self):
        return heapq.heappop(self.heap)

    def vacia(self):
        return len(self.heap) == 0