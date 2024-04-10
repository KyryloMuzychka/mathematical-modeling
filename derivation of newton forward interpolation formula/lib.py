from scipy.interpolate import lagrange
import numpy as np

# Задані дані
x_values = np.array([1.45, 1.6, 1.75, 1.9])
y_values = np.array([1.9696, 1.9978, 1.9035, 1.6344])
xi = 1.48  # Значення аргументу, для якого потрібно знайти похідні

# Побудова інтерполяційного полінома
poly = lagrange(x_values, y_values)
print()
print(poly)
print()
# Обчислення значень першої та другої похідних полінома в точці xi
dpoly = poly.deriv()

print()
print(dpoly)
print()

ddpoly = dpoly.deriv()

print()
print(ddpoly)
print()

# Обчислення значень першої та другої похідних в точці xi
first_derivative = dpoly(xi)
second_derivative = ddpoly(xi)

print("Перша похідна в точці xi:", first_derivative)
print("Друга похідна в точці xi:", second_derivative)
