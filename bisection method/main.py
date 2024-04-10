import math
import numexpr as ne
from colorama import Fore, Back


def get_data():
    borders = list()
    with open('f(x).txt', 'r') as file:
        formula = file.readline()[:-1]
        eps = file.readline()[:-1]
        for line in file:
            pair = list(map(float, line.split()))
            borders.append(pair)
    return formula, borders, float(eps)


def calculate_y(f_x, value):
    x = value
    return ne.evaluate(f_x)


def print_row(n, a, b, c, f_a, f_b, f_c):
    if not n:
        print(Fore.RESET + Back.YELLOW + "{:<3} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                "N", "a", "b", "c", "f(a)", "f(b)", "f(c)", "|b-a|"))
    print(Back.RESET + Fore.GREEN + "{:<3} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f}".format(n, a, b, c, f_a, f_b, f_c, abs(b - a)))


def print_roots(roots):
    print(Fore.CYAN + "Roots:")
    for el in roots:
        print("{:.4f}".format(el))


def print_number_of_splits(number_of_splits):
    print(Fore.RESET + f"Number of splits per cut: {number_of_splits}")


def bisectoin_method(formula, edges, epsilon):
    roots = list()
    for i in range(len(edges)):
        a, b = edges[i][0], edges[i][1]
        number_of_splits = math.ceil(math.log((b - a) / epsilon, 2))
        print_number_of_splits(number_of_splits)
        n = 0
        while True:
            c = (a + b) / 2
            print_row(n, a, b, c, calculate_y(formula, a), calculate_y(formula, b), calculate_y(formula, c))
            if abs(b - a) <= epsilon:
                roots.append(c)
                break
            if not calculate_y(formula, c):
                roots.append(c)
                break
            if calculate_y(formula, a) * calculate_y(formula, c) < 0:
                b = c
            else:
                a = c
            n += 1

    return roots


def main():
    formula, edges, epsilon = get_data()
    roots = bisectoin_method(formula, edges, epsilon)
    print_roots(roots)


if __name__ == '__main__':
    main()
