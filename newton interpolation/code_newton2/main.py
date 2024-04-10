from colorama import Style, Fore
import matplotlib.pyplot as plt


def get_coordinates():
    coodinates = []
    with open("coordinates_test.txt", 'r') as file:
        file.readline()
        xx = float(file.readline()[:-1])
        while True:
            line = file.readline()[:-1]
            if not line:
                break
            coodinates.append([float(i) for i in line.split(' ')])
    return coodinates, xx

def print_info(coordinates, x, y):
    x_array = [format(i[0], '.4f') for i in coordinates]
    y_array = [format(i[1], '.4f') for i in coordinates]
    print(Style.BRIGHT + Fore.CYAN, end='')
    print("x:", end='')
    for i in x_array:
        print(" {:<8}".format(i), end='')
    print("\ny:", end='')
    for i in y_array:
        print(" {:<8}".format(i), end='')
    print("\nX =", x)
    print(Style.BRIGHT + Fore.RED, end='')
    print("y(X) =", format(y, '.4f'))
    
    
def add_point(coordinates, x, y):
    for i in range(len(coordinates)):
        if x <= coordinates[i][0]:
            coordinates.insert(i, [x, y])
            break


def drow_plot(coordinates):
    x = [i[0] for i in coordinates]
    y = [i[1] for i in coordinates]

    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.plot(x, y, color='red', linestyle='solid', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    plt.show()


def newton2(coordinates, xx):
    x = []
    y = []    
    for i in coordinates:
        x.append(i[0])
        y.append(i[1])    
    h = x[1] - x[0]
    n = len(x)
    q = (xx - x[n-1]) / h
    try:
        if abs(q) >= 1:
            raise Exception("|q| >= 1")
        d = [i for i in y]        
        t = 1
        p = d[n-1]
        for k in range(1, n):
            for i in range(n-k):
                d[i] = d[i+1] - d[i]
            t *= (q + k - 1) / k
            r = d[n-k-1] * t
            p += r
        return p
    except Exception as e:
        print(f"{e}")
        return e


def main():
    coordinates, xx = get_coordinates()
    yy = newton2(coordinates, xx)
    if isinstance(yy, float):
        print_info(coordinates, xx, yy)
        add_point(coordinates, xx, yy)
        drow_plot(coordinates)


if __name__ == "__main__":
    main()
