import numpy as np
import math
from typing import List, Tuple
from matplotlib import pyplot as plt
import timeit

def func_py(x: List[float]) -> List[float]:
    """
    Calculate function values for passed array of arguments
    """
    N = 17
    return [math.sin(math.pi * xi / N) for xi in x]

def tabulate_py(a: float, b: float, n: int) -> Tuple[List[float], List[float]]:
    x = [a + i * (b - a) / n for i in range(n)]
    y = func_py(x)
    return x, y

def tabulate_np(a: float, b: float, n: int) -> Tuple[np.ndarray, np.ndarray]:
    x = np.linspace(a, b, n)
    y = x / (x**2 + 1)
    return x, y

def main():
    a, b = 0, 1
    n = np.array((1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000), dtype="uint32")
    t_py = np.zeros(len(n))
    t_np = np.zeros(len(n))
    
    for i in range(len(n)):
        t_py[i] = 1_000_000 * timeit.timeit(f"tabulate_py({a}, {b}, {n[i]})", number=100, globals=globals()) / 100
        t_np[i] = 1_000_000 * timeit.timeit(f"tabulate_np({a}, {b}, {n[i]})", number=100, globals=globals()) / 100

    plt.plot(n, t_py/t_np)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
