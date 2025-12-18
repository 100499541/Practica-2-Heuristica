#!/usr/bin/env python3
import os
# Importa la clase Grafo desde el módulo grafo.py para leer y manipular los grafos
from grafo import Grafo

# Definición de la función principal para crear un vértice aislado
def crear_vertice_aislado(nombre_mapa, vertice_a_aislar, output_prefix):
    # Construye la ruta base del mapa dentro de la carpeta "pruebas-2" y de los archivos .gr y .co
    base_path = os.path.join("pruebas-2", nombre_mapa)
    gr_file = base_path + ".gr"
    co_file = base_path + ".co"

    # Comprueba que los archivos originales existen antes de continuar
    if not os.path.exists(gr_file) or not os.path.exists(co_file):
        print("No se encuentran los ficheros originales")
        return

    # Crear un objeto Grafo y leer los archivos .gr y .co
    grafo = Grafo()
    grafo.leer_gr(gr_file)
    grafo.leer_co(co_file)

    # Eliminar todos los arcos salientes del vértice a aislar
    if vertice_a_aislar in grafo.arcos:
        del grafo.arcos[vertice_a_aislar]
    # Eliminar todos los arcos entrantes hacia el vértice a aislar
    for v, lista in grafo.arcos.items():
        grafo.arcos[v] = [(dest, cost) for (dest, cost) in lista if dest != vertice_a_aislar]

    # Definir los nombres de los archivos de salida modificados dentro de la carpeta "pruebas-2"
    new_gr_file = os.path.join("pruebas-2", output_prefix + ".gr")
    new_co_file = os.path.join("pruebas-2", output_prefix + ".co")

    # Guardar el archivo .gr con los arcos modificados
    with open(new_gr_file, "w") as f:
        for origen, lista in grafo.arcos.items():
            for destino, coste in lista:
                f.write(f"a {origen} {destino} {coste}\n")

    # Guardar el archivo .co con las coordenadas originales
    with open(new_co_file, "w") as f:
        for v, (lon, lat) in grafo.coordenadas.items():
            # Guardamos en formato DIMACS: enteros multiplicados por 1e6
            f.write(f"v {v} {int(lon*1e6)} {int(lat*1e6)}\n")

    # Mensajes finales informativos
    print(f"Grafo modificado guardado en {new_gr_file} y {new_co_file}")
    print(f"Vértice aislado: {vertice_a_aislar}")

# Bloque principal para ejecutar la función desde la línea de comandos
if __name__ == "__main__":
    import sys
    # Comprobar que se han pasado exactamente 3 argumentos
    if len(sys.argv) != 4:
        print("Uso: python crear-aislado.py nombre-mapa vertice-a-aislar prefijo-salida")
    else:
        # Asignar los argumentos a variables
        nombre_mapa = sys.argv[1]
        vertice_a_aislar = int(sys.argv[2])
        prefijo_salida = sys.argv[3]
        # Llamar a la función principal
        crear_vertice_aislado(nombre_mapa, vertice_a_aislar, prefijo_salida)