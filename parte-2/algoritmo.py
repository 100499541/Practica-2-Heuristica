# algoritmo.py
import math
import time
from abierta import Abierta
from cerrada import Cerrada

class Algoritmo:
    def __init__(self, grafo):
        self.grafo = grafo
        self.nodos_expandidos = 0

    def heuristica(self, u, v):
        """Distancia aproximada en metros usando fórmula euclídea"""
        lat1, lon1 = self.grafo.coordenadas[u]
        lat2, lon2 = self.grafo.coordenadas[v]
        dx = (lon2 - lon1) * 111320  # metros por grado longitud
        dy = (lat2 - lat1) * 110540  # metros por grado latitud
        return math.sqrt(dx**2 + dy**2)

    def buscar_A_estrella(self, inicio, fin):
        """Algoritmo A* con heurística basada en coordenadas"""
        abierta = Abierta()
        cerrada = Cerrada()
        abierta.push(0, inicio, [inicio])
        costo_g = {inicio: 0}

        while not abierta.vacia():
            coste_actual, nodo, path = abierta.pop()
            if nodo == fin:
                return path, coste_actual, self.nodos_expandidos
            if cerrada.contiene(nodo):
                continue
            cerrada.add(nodo)
            self.nodos_expandidos += 1

            for vecino, coste_arco in self.grafo.vecinos(nodo):
                nuevo_g = costo_g[nodo] + coste_arco
                if vecino not in costo_g or nuevo_g < costo_g[vecino]:
                    costo_g[vecino] = nuevo_g
                    f = nuevo_g + self.heuristica(vecino, fin)
                    abierta.push(f, vecino, path + [vecino])
        return None, float('inf'), self.nodos_expandidos

    def buscar_Dijkstra(self, inicio, fin):
        """Versión fuerza bruta (Dijkstra)"""
        # Dijkstra es A* con heurística 0
        return self.buscar_A_estrella_sin_heuristica(inicio, fin)

    def buscar_A_estrella_sin_heuristica(self, inicio, fin):
        """A* sin heurística = Dijkstra"""
        abierta = Abierta()
        cerrada = Cerrada()
        abierta.push(0, inicio, [inicio])
        costo_g = {inicio: 0}

        while not abierta.vacia():
            coste_actual, nodo, path = abierta.pop()
            if nodo == fin:
                return path, coste_actual, self.nodos_expandidos
            if cerrada.contiene(nodo):
                continue
            cerrada.add(nodo)
            self.nodos_expandidos += 1

            for vecino, coste_arco in self.grafo.vecinos(nodo):
                nuevo_g = costo_g[nodo] + coste_arco
                if vecino not in costo_g or nuevo_g < costo_g[vecino]:
                    costo_g[vecino] = nuevo_g
                    f = nuevo_g  # sin heurística
                    abierta.push(f, vecino, path + [vecino])
        return None, float('inf'), self.nodos_expandidos
