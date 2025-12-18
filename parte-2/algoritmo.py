# Módulos de Python para cálculos matemáticos y tiempos de ejecución
import math
from abierta import Abierta  # Importa la lista abierta para nodos por visitar
from cerrada import Cerrada  # Importa la lista cerrada para nodos visitados

class Algoritmo:
    # Clase que implementa algoritmos de búsqueda de caminos en un grafo:
    # A* (con heurística euclídea) y Dijkstra (A* sin heurística)
    def __init__(self, grafo):
        self.grafo = grafo                # Guarda el objeto Grafo con arcos y coordenadas
        self.nodos_expandidos = 0         # Contador de nodos visitados durante la búsqueda

    def heuristica(self, u, v):
        # Calcula distancia aproximada entre dos nodos usando coordenadas geográficas
        # Retorna distancia euclídea en metros

        # Nuevo: si alguno de los nodos no existe en el diccionario de coordenadas,
        # devolvemos 0 para evitar error y permitir que el algoritmo siga expandiendo
        if u not in self.grafo.coordenadas or v not in self.grafo.coordenadas:
            return 0

        lat1, lon1 = self.grafo.coordenadas[u]  # Coordenadas del nodo u
        lat2, lon2 = self.grafo.coordenadas[v]  # Coordenadas del nodo v
        dx = (lon2 - lon1) * 111320            # Conversión de grados longitud a metros
        dy = (lat2 - lat1) * 110540            # Conversión de grados latitud a metros
        return math.sqrt(dx**2 + dy**2)        # Distancia euclídea

    def buscar_A_estrella(self, inicio, fin):
        # Implementa el algoritmo A* con:
        # abierta: lista de nodos por visitar con su coste estimado
        # cerrada: nodos ya visitados
        # costo_g: coste acumulado desde el inicio hasta cada nodo
        abierta = Abierta()
        cerrada = Cerrada()
        abierta.push(0, inicio, [inicio])   # Se añade el nodo inicial con coste 0 y ruta inicial
        costo_g = {inicio: 0}

        # Mientras queden nodos por explorar
        while not abierta.vacia():
            # Tomar nodo con menor coste estimado f = g + h
            coste_actual, nodo, path = abierta.pop()

            # Si llegamos al nodo destino
            if nodo == fin:
                # Devolver ruta, coste y nodos expandidos       
                return path, coste_actual, self.nodos_expandidos

            # Si ya visitamos este nodo, saltar
            if cerrada.contiene(nodo):
                continue

            # Marcar nodo como visitado
            cerrada.add(nodo)
            # Incrementar contador de nodos expandidos
            self.nodos_expandidos += 1

            # Explorar vecinos del nodo actual
            for vecino, coste_arco in self.grafo.vecinos(nodo):
                # Calcular coste acumulado hasta vecino
                nuevo_g = costo_g[nodo] + coste_arco
                # Si no se ha visitado o encontramos camino más barato
                if vecino not in costo_g or nuevo_g < costo_g[vecino]:
                    costo_g[vecino] = nuevo_g
                    # Coste total estimado = g + h
                    f = nuevo_g + self.heuristica(vecino, fin)
                    # Añadir vecino a la lista abierta con ruta actualizada
                    abierta.push(f, vecino, path + [vecino])

        # Si no se encuentra ruta, devolver infinito
        return None, float('inf'), self.nodos_expandidos

    def buscar_Dijkstra(self, inicio, fin):
        # Implementa Dijkstra
        # Es equivalente a A* sin heurística, delega en buscar_A_estrella_sin_heuristica
        return self.buscar_A_estrella_sin_heuristica(inicio, fin)

    def buscar_A_estrella_sin_heuristica(self, inicio, fin):
        # A* sin heurística = Dijkstra
        # El coste f = g, es decir, sólo el coste acumulado desde inicio
        abierta = Abierta()
        cerrada = Cerrada()
        abierta.push(0, inicio, [inicio])   # Nodo inicial con coste 0
        costo_g = {inicio: 0}               # Coste acumulado inicial

        # Mientras queden nodos por explorar
        while not abierta.vacia():
            # Tomar nodo con menor coste g
            coste_actual, nodo, path = abierta.pop()

            # Si llegamos al destino marcarlo
            if nodo == fin:
                return path, coste_actual, self.nodos_expandidos

            # Saltar si ya visitado
            if cerrada.contiene(nodo):
                continue

            # Marcar el nodo como visitado
            cerrada.add(nodo)
            # Aumentar el contador de nodos expandidos
            self.nodos_expandidos += 1

            # Explorar vecinos
            for vecino, coste_arco in self.grafo.vecinos(nodo):
                nuevo_g = costo_g[nodo] + coste_arco       # Coste acumulado
                if vecino not in costo_g or nuevo_g < costo_g[vecino]:
                    costo_g[vecino] = nuevo_g
                    f = nuevo_g                            # Sin heurística
                    # Añadir a la lista abierta con la ruta
                    abierta.push(f, vecino, path + [vecino])

        # Si no se encuentra ruta
        return None, float('inf'), self.nodos_expandidos