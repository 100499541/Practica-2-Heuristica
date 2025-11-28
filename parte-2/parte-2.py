#!/usr/bin/env python3
import sys
import time
import os
from grafo import Grafo
from algoritmo import Algoritmo

def main():
    # Comprobar que se pasan exactamente 5 argumentos
    if len(sys.argv) != 5:
        print("Uso: python parte-2.py vertice-1 vertice-2 nombre-del-mapa fichero-salida")
        return

    # Asignar los argumentos a variables
    inicio = int(sys.argv[1])
    fin = int(sys.argv[2])
    nombre_mapa = sys.argv[3]
    fichero_salida = sys.argv[4]

    # Si el nombre del mapa no es ruta absoluta y no existe en el directorio actual,
    # buscar en la carpeta 'pruebas-2' y guardar también el fichero de salida ahí
    if not os.path.isabs(nombre_mapa) and not os.path.exists(nombre_mapa + ".gr"):
        nombre_mapa = os.path.join("pruebas-2", nombre_mapa)
        fichero_salida = os.path.join("pruebas-2", fichero_salida)

    grafo_file = nombre_mapa + ".gr"
    coord_file = nombre_mapa + ".co"

    # Crear objeto Grafo y leer archivos .gr y .co
    grafo = Grafo()
    grafo.leer_gr(nombre_mapa + ".gr")
    grafo.leer_co(nombre_mapa + ".co")

    # Mostrar número de vértices y arcos
    print(f"# vertices: {len(grafo.coordenadas)}")
    num_arcos = sum(len(v) for v in grafo.arcos.values())
    print(f"# arcos : {num_arcos}")

    # Resolver con algoritmo A* eficiente
    alg = Algoritmo(grafo)
    t0 = time.time()
    ruta, coste_total, nodos_expandidos = alg.buscar_A_estrella(inicio, fin)
    t1 = time.time()

    # Mostrar resultados por pantalla
    print(f"Solución óptima encontrada con coste {coste_total}")
    print(f"Tiempo de ejecución: {t1 - t0:.2f} segundos")
    print(f"# expansiones : {nodos_expandidos}")

    # Escribir fichero de salida
    with open(fichero_salida, 'w') as f:
        if ruta:
            # Si hay ruta, escribir todos los vértices y costes de arcos
            for i in range(len(ruta)-1):
                arco_coste = dict(grafo.arcos[ruta[i]])[ruta[i+1]]
                f.write(f"{ruta[i]} - ({arco_coste}) - ")
            f.write(f"{ruta[-1]}\n")
        else:
            # Si no hay camino posible (es decir, es infactible), escribir "Caso infactible"
            f.write("Caso infactible\n")

if __name__ == "__main__":
    main()