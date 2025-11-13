#!/usr/bin/env python3
import sys
from constraint import Problem, ExactSumConstraint
import random

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    n = len(lines)
    grid = []
    for line in lines:
        grid.append(list(line))
    return n, grid

def print_grid(grid):
    n = len(grid)
    print("+---"*n + "+")
    for row in grid:
        print("| " + " | ".join(row) + " |")
    print("+---"*n + "+")

def convert_grid_to_display(grid):
    """Convierte 0/1 a O/X para mostrar o guardar"""
    return [['O' if cell == 0 else 'X' for cell in row] for row in grid]

def main():
    if len(sys.argv) != 3:
        print("Uso: python parte-1.py fichero-entrada.in fichero-salida.out")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

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

    # Restricciones: no más de dos iguales consecutivos en filas
    for i in range(n):
        for j in range(n-2):
            problem.addConstraint(
                lambda a,b,c: not (a==b==c),
                [(i,j), (i,j+1), (i,j+2)]
            )

    # Restricciones: no más de dos iguales consecutivos en columnas
    for j in range(n):
        for i in range(n-2):
            problem.addConstraint(
                lambda a,b,c: not (a==b==c),
                [(i,j), (i+1,j), (i+2,j)]
            )

    # Restricciones: mismo número de O y X en cada fila y columna
    half_n = n // 2
    for i in range(n):
        problem.addConstraint(ExactSumConstraint(half_n), [(i,j) for j in range(n)])
    for j in range(n):
        problem.addConstraint(ExactSumConstraint(half_n), [(i,j) for i in range(n)])

    # Resolver
    solutions = problem.getSolutions()
    print(f"{len(solutions)} soluciones encontradas")

    # Escribir salida
    with open(output_file, 'w') as f:
        # Instancia original
        f.write("+---"*n + "+\n")
        for row in grid:
            f.write("| " + " | ".join(row) + " |\n")
        f.write("+---"*n + "+\n")

        # Primera solución (elegida aleatoriamente entre las posibles)
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