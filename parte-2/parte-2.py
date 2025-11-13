#!/usr/bin/env python3
import sys
import time
from grafo import Grafo
from algoritmo import Algoritmo

def main():
    if len(sys.argv) != 5:
        print("Uso: ./parte-2.py vertice-1 vertice-2 nombre-del-mapa fichero-salida")
        return

    inicio = int(sys.argv[1])
    fin = int(sys.argv[2])
    nombre_mapa = sys.argv[3]
    fichero_salida = sys.argv[4]

    # Leer grafo y coordenadas
    grafo = Grafo()
    grafo.leer_gr(nombre_mapa + ".gr")
    grafo.leer_co(nombre_mapa + ".co")

    print(f"# vertices: {len(grafo.coordenadas)}")
    num_arcos = sum(len(v) for v in grafo.arcos.values())
    print(f"# arcos : {num_arcos}")

    # Resolver con algoritmo A* eficiente
    alg = Algoritmo(grafo)
    t0 = time.time()
    ruta, coste_total, nodos_expandidos = alg.buscar_A_estrella(inicio, fin)
    t1 = time.time()

    print(f"Solución óptima encontrada con coste {coste_total}")
    print(f"Tiempo de ejecución: {t1 - t0:.2f} segundos")
    print(f"# expansiones : {nodos_expandidos}")

    # Escribir fichero de salida
    if ruta:
        with open(fichero_salida, 'w') as f:
            for i in range(len(ruta)-1):
                arco_coste = dict(grafo.arcos[ruta[i]])[ruta[i+1]]
                f.write(f"{ruta[i]} - ({arco_coste}) - ")
            f.write(f"{ruta[-1]}\n")

if __name__ == "__main__":
    main()