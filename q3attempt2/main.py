import numpy as np
from numpy.polynomial import Polynomial as P
from functools import lru_cache
import scipy.integrate
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

#Define the recurrence relation to get the coefficents for the series solution
def recurrence_relation(n:int,a0:int,a1:int) -> np.array:
    a = [a0,a1]
    for N in range(0, n-2):
        an = ((2-(N*(N-1)))*a[N]/((N+1) * (N+2)))
        a.append(an)
    return np.array(a)

#Generate the series solutions, where iterations are the number of terms we want
def series(iterations:int) -> np.polynomial:
    
    a0_coeff = recurrence_relation(iterations, a0=1, a1=0)
    a1_coeff = recurrence_relation(iterations, a0=0, a1=1)

    y0_poly = P(a0_coeff)
    y1_poly = P(a1_coeff)

    return y0_poly, y1_poly

#Define the exact solution that has been manually calculated to later plot
def exact_solution():
    return sp.lambdify(x, (1/4 + x/2 * sp.atan(x) + (1+x**2)/4 * (sp.atan(x))**2), modules=['numpy'])


def sketch_series_solutions(y0_poly, y1_poly):

    x = np.linspace(-3,3,num=100)

    solution = exact_solution()

    # plt.plot(x,y0_poly(x),label="y=1+x^2")
    # plt.plot(x, y1_poly(x), label="y=x+x^3/3-x^5/15+...")
    plt.plot(x, y0_poly(x) + y1_poly(x), label="y=solution") #General solution is the sum of these
    plt.plot(x, solution(x), label="exact solution")
    plt.xlim(-3,3)
    plt.ylim(-10,10)
    plt.show()


def main():
    y0_poly, y1_poly = series(100000) #Place holder, will calculate 8 terms (since a0, a1 already defined)
    sketch_series_solutions(y0_poly, y1_poly)

if __name__ == "__main__":
    main()


