import scipy.integrate as spi
import random


def f(x):
    return 2 * x - x ** 2

def monte_carlo_integration(func, a, b, n):
    total = 0
    for _ in range(n):
        x = random.uniform(a, b)
        total += func(x)
    return total / n * (b - a)

a = 0 
b = 2  
n = 10000000  

monte_carlo_result = monte_carlo_integration(f, a, b, n)
print("Значення інтегралу обчислене методом Монте-Карло:", monte_carlo_result)

quad_result, error = spi.quad(f, a, b)
print("Значення інтегралу обчислене функцією quad: ", quad_result)
