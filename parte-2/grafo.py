# Definimos la clase Grafo para representar un grafo con arcos y coordenadas
class Grafo:

    def __init__(self):
        # Diccionario que guarda los arcos de cada nodo
        # Clave: nodo origen, Valor: lista de tuplas (nodo destino, coste)
        self.arcos = {}        

        # Diccionario que guarda las coordenadas de cada nodo
        # Clave: nodo, Valor: tupla (latitud, longitud)
        self.coordenadas = {}  

    # Método para leer el archivo .gr y construir los arcos del grafo
    def leer_gr(self, archivo_gr):
        # Leemos el fichero y construimos los arcos
        with open(archivo_gr, 'r') as f:
            for line in f:
                if line.startswith('a'):
                    # Cada línea tiene formato: a nodo u nodo v coste
                    _, u, v, coste = line.strip().split()
                    u, v, coste = int(u), int(v), int(coste)
                    # Si el nodo origen no está en el diccionario de arcos, se crea la lista vacía
                    if u not in self.arcos:
                        self.arcos[u] = []
                    # Añadimos el arco (destino, coste) a la lista de arcos del nodo u
                    self.arcos[u].append((v, coste))

    # Método para leer el archivo .co y guardar las coordenadas de los nodos
    def leer_co(self, archivo_co):
        # Leemos el fichero y guardamos las coordenadas
        with open(archivo_co, 'r') as f:
            for line in f:
                if line.startswith('v'):
                    # Cada línea tiene formato: v nodo longitud latitud
                    _, nodo, lon, lat = line.strip().split()
                    nodo = int(nodo)
                    # Convertimos las coordenadas enteras a flotante
                    lon, lat = int(lon)/1e6, int(lat)/1e6
                    # Guardamos las coordenadas en el diccionario
                    self.coordenadas[nodo] = (lat, lon)

    # Método que devuelve los vecinos y costes de un nodo dado
    def vecinos(self, nodo):
        # Devuelve la lista de tuplas (vecino, coste) del nodo, o lista vacía si no existe
        return self.arcos.get(nodo, [])
