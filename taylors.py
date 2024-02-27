import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, series, lambdify
import re

import re
from sympy import sympify


def input_function():
    """Get the function input from the user and format it for sympify."""
    func = input("Enter the function (in terms of 'x'): ")
    func = func.replace('^', '**')
    func = re.sub(r'(\d|\))(\(|[a-zA-Z])', r'\1*\2', func)
    func = re.sub(r'(\d|x)(x|\d)', r'\1*\2', func)
    return func


if __name__ == "__main__":
    f = input_function()
    try:
        sympy_expr = sympify(f)
        print(f"Valid sympy expression: {sympy_expr}")
    except Exception as e:
        print(f"Invalid input: {f}")
        print(e)


def input_taylor_degree():
    """get the TS deg"""
    return int(input("Enter the degree of the Taylor series: "))

def input_window():
    """get window settings"""
    x_min = float(input("Enter the minimum x value: "))
    x_max = float(input("Enter the maximum x value: "))
    y_min = float(input("Enter the minimum y value: "))
    y_max = float(input("Enter the maximum y value: "))
    return (x_min, x_max, y_min, y_max)

def input_center_point():
    """get center point for TS"""
    return float(input("Enter the center point 'a' for the Taylor series: "))

def main():
    func_input = input_function()
    taylor_degree = input_taylor_degree()
    window = input_window()
    center_point = input_center_point()
    x = symbols('x')
    func = sympify(func_input)
    taylor_series = series(func, x, center_point, taylor_degree + 1).removeO()
    print(f"Taylor series before lambdify: {taylor_series}")
    x_vals = np.linspace(window[0], window[1], 500)
    taylor_func = lambdify(x, taylor_series, modules=['numpy'])

    if np.isscalar(taylor_series):
        taylor_vals = np.full_like(x_vals, taylor_series)
    else:
        taylor_vals = taylor_func(x_vals)

    # Debugging print statements
    print(f"x_vals shape: {x_vals.shape}")
    print(f"taylor_vals shape: {np.shape(taylor_vals)}")

    try:
        # Plotting
        plt.figure(figsize=(10, 6))
        y_vals = lambdify(x, func, modules=['numpy'])(x_vals)
        plt.plot(x_vals, y_vals, label='Function')
        plt.plot(x_vals, taylor_vals, label=f'Taylor Approximation (Degree {taylor_degree})', linestyle='--')
        plt.xlim(window[0], window[1])
        plt.ylim(window[2], window[3])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Function and its Taylor Series Approximation')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")

    print(f"The Taylor polynomial approximation is: \n{taylor_series}")


if __name__ == "__main__":
    main()
