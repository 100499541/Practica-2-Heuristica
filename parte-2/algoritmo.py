# algoritmo.py
import time
from abierta import Abierta
from cerrada import Cerrada
import math

class Algoritmo:
    def __init__(self, grafo):
        self.grafo = grafo
        self.nodos_expandidos = 0

    def heuristica(self, u, v):
        """Distancia aproximada entre coordenadas (Haversine)"""
        lat1, lon1 = self.grafo.coordenadas[u]
        lat2, lon2 = self.grafo.coordenadas[v]
        # Aproximación simple euclídea en metros
        dx = (lon2 - lon1) * 111320  # metros aproximados por grado
        dy = (lat2 - lat1) * 110540
        return (dx**2 + dy**2)**0.5

    def buscar_A_estrella(self, inicio, fin):
        """Implementación de A* (o Dijkstra si heurística = 0)"""
        abierta = Abierta()
        cerrada = Cerrada()
        abierta.push(0, inicio, [inicio])
        while not abierta.vacia():
            coste_actual, nodo, path = abierta.pop()
            if nodo == fin:
                return path, coste_actual, self.nodos_expandidos
            if cerrada.contiene(nodo):
                continue
            cerrada.add(nodo)
            self.nodos_expandidos += 1
            for vecino, coste in self.grafo.vecinos(nodo):
                if not cerrada.contiene(vecino):
                    nuevo_coste = coste_actual + coste
                    nueva_ruta = path + [vecino]
                    abierta.push(nuevo_coste, vecino, nueva_ruta)
        return None, float('inf'), self.nodos_expandidos

    def buscar_Dijkstra(self, inicio, fin):
        """Versión fuerza bruta (heurística = 0)"""
        return self.buscar_A_estrella(inicio, fin)  # heurística = 0
