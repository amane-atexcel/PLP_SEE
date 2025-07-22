from sympy import symbols, solve   #Installing the packing is very important, so go to your terminal and type pip install sympy

x = symbols('x')
# Solve for x in x**2 + 5*x + 6 = 0
equation = x**2 + 5*x + 6
solutions = solve(equation, x)
print(f"Solutions: {solutions}") # Outputs [-3, -2]