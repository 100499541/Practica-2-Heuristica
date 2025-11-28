#!/usr/bin/env python3
import sys
import os
import matplotlib.pyplot as plt
from grafo import Grafo

def detectar_vertices_aislados(grafo):
    """Devuelve la lista de vértices sin arcos (aislados)."""
    vertices_aislados = []
    for v in grafo.coordenadas.keys():
        if v not in grafo.arcos or len(grafo.arcos[v]) == 0:
            vertices_aislados.append(v)
    return vertices_aislados

def main():
    if len(sys.argv) != 3:
        print("Uso: python ver_mapa.py USA-road-d.BAY fichero_aislados.txt")
        return

    nombre_mapa = sys.argv[1]
    fichero_aislados = sys.argv[2]

    # Ajustar ruta a carpeta pruebas-2
    base_path = os.path.join("pruebas-2", nombre_mapa)
    coord_file = base_path + ".co"
    gr_file = base_path + ".gr"

    if not os.path.exists(coord_file) or not os.path.exists(gr_file):
        print(f"No se encuentra alguno de los ficheros: {coord_file} o {gr_file}")
        return

    # Cargar grafo
    grafo = Grafo()
    grafo.leer_gr(gr_file)
    grafo.leer_co(coord_file)

    # Detectar vértices aislados
    vertices_aislados = detectar_vertices_aislados(grafo)
    with open(fichero_aislados, "w") as f:
        for v in vertices_aislados:
            f.write(f"{v}\n")
    print(f"Se han encontrado {len(vertices_aislados)} vértices aislados")
    print(f"IDs guardados en {fichero_aislados}")

    # Extraer coordenadas para dibujar mapa
    xs = []
    ys = []
    for v, (lon, lat) in grafo.coordenadas.items():
        xs.append(lon / 1e6)
        ys.append(lat / 1e6)

    # Dibujar mapa
    plt.figure(figsize=(8, 8))
    plt.scatter(xs, ys, s=1, color='blue')
    plt.title(f"Mapa: {nombre_mapa}")
    plt.xlabel("Longitud")
    plt.ylabel("Latitud")
    plt.axis("equal")
    plt.show()

if __name__ == "__main__":
    main()