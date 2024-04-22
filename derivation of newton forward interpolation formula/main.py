from sympy import diff, symbols
from colorama import Fore


def get_coordinates():
    coordinates = []
    with open("coordinates.txt", 'r') as file:
        file.readline()
        xx = float(file.readline()[:-1])
        while True:
            line = file.readline()[:-1]
            if not line:
                break
            coordinates.append([float(i) for i in line.split(' ')])
    return coordinates, xx


def product(val, n, x):
    mul = 1
    for i in range(n):
        if i:
            mul *= val - x[i-1]
        yield mul


def get_coefficients(x, y):
    n = len(x)
    F = [[0] * n for _ in range(n)]
    
    for i in range(n):
        F[i][0] = y[i]       
        
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = round((F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i]), 4)
            # print(str('(' + str(F[i + 1][j - 1])) + ' - ' + str(F[i][j - 1])  + ') / (' + str(x[i + j]) + ' - ' + str(x[i]) + ')' + ' = '+ str(F[i][j]))            
        # print()    
          
    # for j in range(1, n):
    #     for i in range(n - j):            
    #         print(F[i][j], end='  ')
    #     print()       
            
    return [F[0][i] for i in range(n)]


def main():
    coordinates, xx = get_coordinates()    
    
    x = [i[0] for i in coordinates]
    y = [i[1] for i in coordinates]        
    
    x_sym = symbols('x')
    
    C = get_coefficients(x, y)
    
    # print()
    # for k, p in enumerate(product(x_sym, len(C), x)):
    #     print(k, ' ', C[k], '   ', p, '    ' ,C[k] * p)
    
    poly = sum(C[k] * p for k, p in enumerate(product(x_sym, len(C), x)))     
    f_xx = poly.subs(x_sym, xx)
    
    derivative_poly = diff(poly, x_sym)
    first_derivative = derivative_poly.subs(x_sym, xx)

    dderivative_poly = diff(derivative_poly, x_sym)
    second_derivative = dderivative_poly.subs(x_sym, xx)

    print(Fore.GREEN, "Поліном:\n", poly)
    print(Fore.BLUE, "Значення полінома у точці x = " + str(xx) + ": " + str(round(f_xx, 4)) + "\n")
      

    print(Fore.GREEN, "Похідна першого порядку:\n", derivative_poly)
    print(Fore.BLUE, "Похідна першого порядку в точці x = " + str(xx) + ": " + str(round(first_derivative, 4)) + "\n")
    
    
    print(Fore.GREEN, "Похідна другого порядку:\n", dderivative_poly)
    print(Fore.BLUE, "Похідна другого порядку в точці x = " + str(xx) + ": " + str(round(second_derivative, 4)) + Fore.RESET)       


if __name__ == "__main__":
    main()