#!/usr/bin/env python3
import sys
from constraint import Problem, ExactSumConstraint
import random

# Función para leer el fichero .in donde esta el tablero problema
def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    n = len(lines)
    # Crea el tablero (grid) donde se resuelve el problema y lo llena con el tablero problema
    grid = []
    for line in lines:
        grid.append(list(line))
    return n, grid

# Función para imprimir los tableros
def print_grid(grid):
    n = len(grid)
    print("+---"*n + "+")
    for row in grid:
        print("| " + " | ".join(row) + " |")
    print("+---"*n + "+")

# Función para convertir 0/1 a O/X para mostrarlo correctamente
def convert_grid_to_display(grid):
    return [['O' if cell == 0 else 'X' for cell in row] for row in grid]

# Main que ejecuta todo el proceso
def main():
    # Comprueba que se ha ejecutado correctamente el comando y da error si no se ha hecho
    if len(sys.argv) != 3:
        print("Uso: python parte-1.py fichero-entrada.in fichero-salida.out")
        return

    # Guarda los archivos .in y .out en variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Lee e imprime por pantalla el archivo .in del tablero problema
    n, grid = read_input(input_file)
    print("Instancia a resolver:")
    print_grid(grid)

    # Crear problema CSP
    problem = Problem()

    # Variables y dominios (0 = O, 1 = X)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                problem.addVariable((i,j), [0,1])
            elif grid[i][j] == 'O':
                problem.addVariable((i,j), [0])
            elif grid[i][j] == 'X':
                problem.addVariable((i,j), [1])

    # Primera restricción: no más de dos iguales consecutivos en filas
    for i in range(n):
        for j in range(n-2):
            problem.addConstraint(
                lambda a,b,c: not (a==b==c),
                [(i,j), (i,j+1), (i,j+2)]
            )

    # Segunda restricción no más de dos iguales consecutivos en columnas
    for j in range(n):
        for i in range(n-2):
            problem.addConstraint(
                lambda a,b,c: not (a==b==c),
                [(i,j), (i+1,j), (i+2,j)]
            )

    # Tercera restricción: mismo número de O y X en cada fila y columna
    half_n = n // 2
    for i in range(n):
        problem.addConstraint(ExactSumConstraint(half_n), [(i,j) for j in range(n)])
    for j in range(n):
        problem.addConstraint(ExactSumConstraint(half_n), [(i,j) for i in range(n)])

    # Resolver el problema e imprimir una solución de forma aleatoria (ya que hay varias soluciones)
    solutions = problem.getSolutions()
    print(f"{len(solutions)} soluciones encontradas")

    # Escribir el archivo de salida .out 
    with open(output_file, 'w') as f:
        # Escribir tablero original
        f.write("+---"*n + "+\n")
        for row in grid:
            f.write("| " + " | ".join(row) + " |\n")
        f.write("+---"*n + "+\n")

        # Elegir una solución (aleatoriamente entre las posibles) y escribirla
        if solutions:
            sol = random.choice(solutions)
            f.write("+---"*n + "+\n")
            for i in range(n):
                row = [sol[(i,j)] for j in range(n)]
                row_display = ['O' if x == 0 else 'X' for x in row]
                f.write("| " + " | ".join(row_display) + " |\n")
            f.write("+---"*n + "+\n")

if __name__ == "__main__":
    main()