import numexpr as ne
from colorama import Fore, Style


def get_data():    
    with open('f(x).txt', 'r') as file:
        formula = file.readline()[:-1]
        a = file.readline()[0:3]
        b = file.readline()[0:3]
        n = file.readline()[0]
    return formula, float(a),  float(b), int(n)


def calculate_y(f_x, value):
    x = value
    return ne.evaluate(f_x)


def left_endpoint_rectangle_method(formula, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + i * h
        s += calculate_y(formula, x)
    s *= h
    return s


def right_endpoint_rectangle_method(formula, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(1, n + 1):
        x = a + i * h
        s += calculate_y(formula, x)
    s *= h    
    return s


def midpoint_rectangle_method(formula, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + (i + 0.5) * h
        s += calculate_y(formula, x)
    s *= h       
    return s


def trapezium_rule(formula, a, b, n):
    h = (b - a) / n
    s = calculate_y(formula, a) + calculate_y(formula, b)
    for i in range(1, n):
        x = a + i * h
        s += 2 * calculate_y(formula, x)
    s *= h / 2
    return s    


def simpson_rule(formula, a, b, n):
    h = (b - a) / n
    s = calculate_y(formula, a) + calculate_y(formula, b)
    k = 4
    for i in range(1, n):
        x = a + i * h
        s += k * calculate_y(formula, x)
        k = 6 - k
    s *= h / 3
    return s


def main():
    formula, a, b, n = get_data()
    
    print(f"Integration of {formula} from {a} to {b} with {n} subdivisions:")
    print("Method                 Result")
    print("-" * 30)

    methods = [
        ("Midpoint Rectangle", midpoint_rectangle_method),
        ("Left Endpoint Rectangle", left_endpoint_rectangle_method),
        ("Right Endpoint Rectangle", right_endpoint_rectangle_method),
        ("Trapezium Rule", trapezium_rule),
        ("Simpson's Rule", simpson_rule)
    ]

    for method_name, method_func in methods:
        result = method_func(formula, a, b, n)
        print(f"{method_name:<25} {Fore.GREEN}{round(result, 3)}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()