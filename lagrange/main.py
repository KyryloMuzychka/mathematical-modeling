from colorama import Fore, Style
import matplotlib.pyplot as plt

def get_coordinates():
  array = []
  with open("coordinates.txt", 'r') as file:
    file.readline()
    x = float(file.readline()[:-1])
    while True:
      line = file.readline()
      if not line:
        break    
      array.append([float(i) for i in line[:-1].split(' ')])
  return array, x


def lagrange(coordinates, x):
  result = 0
  for i in range(len(coordinates)):
    numerator = 1
    denominator = 1
    for j in range(len(coordinates)):
      if i != j:
        numerator *= x - coordinates[j][0]
        denominator *= coordinates[i][0] - coordinates[j][0]    
    result += (numerator / denominator) * coordinates[i][1]
  return result


def print_info(coordinates, x, y):
  x_array = [format(i[0], '.4f') for i in coordinates]
  y_array = [format(i[1], '.4f') for i in coordinates]
  print(Style.BRIGHT + Fore.CYAN, end='')      
  print("x:", *x_array)  
  print("y:", *y_array)  
  print("X =", x)
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
  plt.plot(x, y, color='red', linestyle='solid', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
  plt.show()  

def main():
  coordinates, x = get_coordinates()
  y = lagrange(coordinates, x)
  print_info(coordinates, x, y)
  add_point(coordinates, x, y)  
  drow_plot(coordinates)
 

if __name__ == "__main__":
  main()