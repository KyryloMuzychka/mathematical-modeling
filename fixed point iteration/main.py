import numexpr as ne
from colorama import Fore, Back


def get_data():
    borders = list()
    with open('phi_x.txt', 'r') as file:
        formula = file.readline()[:-1]
        epsilon = file.readline()[:-1]
        for line in file:
            pair = list(map(float, line.split()))
            borders.append(pair)
    return formula, borders, float(epsilon)


def calculate(f_x, value):
    x = value
    return ne.evaluate(f_x)


def print_row(n, x_prev, x, dif):
    if not n:
        print(Fore.RESET + Back.YELLOW + "{:<3} {:<10} {:<10} {:<10}".format(
                "N", "x_prev", "x", "dif"))
    print(Back.RESET + Fore.GREEN + "{:<3} {:<10.4f} {:<10.4f} {:<10.4f}".format(n, x_prev, x, dif))


def iteration_method(phi_x, borders, epsilon):
    roots = list()
    for pair in borders:
        x_prev = pair[0]
        n = 0
        while True:
            x = calculate(phi_x, x_prev)
            if abs(x_prev - x) <= epsilon:
                roots.append(x)
                break
            print_row(n, x_prev, x, abs(x_prev-x))
            x_prev = x
            n += 1
    return roots


def info(f_x, edges, eps):
    print(Fore.BLUE + "Data:")
    print("phi(x) = " + f_x)
    print("epsilon = " + str(eps))
    for pair in edges:
        print("a = " + str(pair[0]) + " b = " + str(pair[1]))
    print(Fore.RESET)


def print_roots(roots):
    print(Fore.CYAN)
    print("Roots:")
    for el in roots:
        print("{:.4f}".format(el))


def main():
    phi_x, borders, eps = get_data()
    info(phi_x, borders, eps)
    roots = iteration_method(phi_x, borders, eps)
    print_roots(roots)


if __name__ == "__main__":
    main()
