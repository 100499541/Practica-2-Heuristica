# grafo.py
class Grafo:
    def __init__(self):
        self.arcos = {}        # { nodo: [(vecino, coste), ...] }
        self.coordenadas = {}  # { nodo: (latitud, longitud) }

    def leer_gr(self, archivo_gr):
        """Leer fichero .gr y construir arcos"""
        with open(archivo_gr, 'r') as f:
            for line in f:
                if line.startswith('a'):
                    _, u, v, coste = line.strip().split()
                    u, v, coste = int(u), int(v), int(coste)
                    if u not in self.arcos:
                        self.arcos[u] = []
                    self.arcos[u].append((v, coste))

    def leer_co(self, archivo_co):
        """Leer fichero .co y guardar coordenadas"""
        with open(archivo_co, 'r') as f:
            for line in f:
                if line.startswith('v'):
                    _, nodo, lon, lat = line.strip().split()
                    nodo = int(nodo)
                    lon, lat = int(lon)/1e6, int(lat)/1e6
                    self.coordenadas[nodo] = (lat, lon)

    def vecinos(self, nodo):
        return self.arcos.get(nodo, [])