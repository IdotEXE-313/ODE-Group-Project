from part_one import recurrence_relation, series
import numpy as np
import sympy as sp
from numpy.polynomial import Polynomial as P
import scipy.integrate as sci
import matplotlib.pyplot as plt

y0_solution, y1_solution = series(3)

x = sp.symbols('x')
sol_one = sp.Poly(y0_solution.coef, x).as_expr()

#finds the second linearly independent solution given the first solution to the ODE
def second_solution(p_x):

    return (sol_one * sp.integrate(sp.exp(-sp.integrate(p_x, x)) / sol_one**2,x))

def wronskian(p_x):

    sol_two = second_solution(p_x)
    wronskian = sp.Matrix([
        [sol_one, sol_two],
        [sp.diff(sol_one,x), sp.diff(sol_two,x)]
    ])
    return wronskian.det(), sol_two

def general_solution():

    wronski, sol_two = wronskian(0)
    integrand_one = sol_two * (1 + x**2)**(-2) / wronski
    integrand_two = sol_one * (1+x**2)**(-2) / wronski
    general_sol_one = -sol_one * sp.integrate(integrand_one, x)
    general_sol_two = sol_two * sp.integrate(integrand_two, x)
    return general_sol_one+general_sol_two

if __name__ == "__main__":

    f_numeric = sp.lambdify(x, general_solution(), modules=['numpy'])
    x = np.linspace(-3,3,100)
    y = f_numeric(x)
    plt.plot(x, y, label="general solution")
    plt.show()



