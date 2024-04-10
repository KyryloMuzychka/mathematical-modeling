
import numpy as np
from colorama import Fore


def get_matrix():
    n = int(input("Enter the number of unknowns: "))
    matrix = []
    for row in range(n):
        row_matrix = list(map(float, input().split()))
        matrix.append(row_matrix)
    return np.array(matrix)


def gauss_jordan(matrix):
    n = len(matrix)

    for iteration in range(n):

        lead_row = matrix[iteration]
        lead_element = lead_row[iteration]

        for j in range(iteration, n+1):
            lead_row[j] /= lead_element

        for i in range(n):
            if i != iteration:
                k = matrix[i][iteration] / lead_row[iteration]
                for j in range(iteration, n+1):
                    matrix[i][j] = matrix[i][j] - k * lead_row[j]


def print_roots(matrix):
    n = len(matrix)
    for j in range(n):
        print(Fore.LIGHTCYAN_EX + "x", j+1, " = ", matrix[j][n], sep="", end="   ")
    print(Fore.RESET)


def main():
    matrix = get_matrix()
    gauss_jordan(matrix)
    print(Fore.BLUE)
    print(matrix, "\n")
    print_roots(matrix)


if __name__ == "__main__":
    main()
