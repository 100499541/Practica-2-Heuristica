#!/usr/bin/env python3
import os
from grafo import Grafo

def crear_vertice_aislado(nombre_mapa, vertice_a_aislar, output_prefix):
    """
    Crea una copia del grafo con un vértice aislado.
    vertice_a_aislar: int, ID del vértice a dejar sin conexiones
    output_prefix: prefijo para los archivos de salida (sin extensión)
    """
    base_path = os.path.join("pruebas-2", nombre_mapa)
    gr_file = base_path + ".gr"
    co_file = base_path + ".co"

    if not os.path.exists(gr_file) or not os.path.exists(co_file):
        print("No se encuentran los ficheros originales")
        return

    # Leer el grafo
    grafo = Grafo()
    grafo.leer_gr(gr_file)
    grafo.leer_co(co_file)

    # Eliminar arcos entrantes y salientes del vértice
    if vertice_a_aislar in grafo.arcos:
        del grafo.arcos[vertice_a_aislar]
    for v, lista in grafo.arcos.items():
        grafo.arcos[v] = [(dest, cost) for (dest, cost) in lista if dest != vertice_a_aislar]

    # Guardar nuevos archivos .gr y .co
    new_gr_file = output_prefix + ".gr"
    new_co_file = output_prefix + ".co"

    with open(new_gr_file, "w") as f:
        for origen, lista in grafo.arcos.items():
            for destino, coste in lista:
                f.write(f"a {origen} {destino} {coste}\n")

    with open(new_co_file, "w") as f:
        for v, (lon, lat) in grafo.coordenadas.items():
            # Guardamos en formato DIMACS: enteros multiplicados por 1e6
            f.write(f"v {v} {int(lon*1e6)} {int(lat*1e6)}\n")

    print(f"Grafo modificado guardado en {new_gr_file} y {new_co_file}")
    print(f"Vértice aislado: {vertice_a_aislar}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uso: python crear_aislado.py nombre_mapa vertice_a_aislar prefijo_salida")
    else:
        nombre_mapa = sys.argv[1]
        vertice_a_aislar = int(sys.argv[2])
        prefijo_salida = sys.argv[3]
        crear_vertice_aislado(nombre_mapa, vertice_a_aislar, prefijo_salida)