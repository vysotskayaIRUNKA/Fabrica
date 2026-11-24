import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

x = sp.symbols('x')
y = sp.Function('y')
diffeq = sp.Eq(y(x).diff(x), -2 * y(x))
sol_sym = sp.dsolve(diffeq, y(x), ics={y(0): sp.sqrt(2)})
print(sol_sym)

y_sym_func = sp.lambdify(x, sol_sym.rhs, modules=['numpy'])

def ode_system(x, y):
    return -2 * y

x_span = (0, 10)
x_eval = np.linspace(0, 10, 200)
y0 = [np.sqrt(2)]

sol_num = solve_ivp(ode_system, x_span, y0, t_eval=x_eval, method='RK45')
y_num_func = sol_num.y[0]

plt.figure(figsize=(10, 5))
plt.plot(x_eval, y_sym_func(x_eval), label='SymPy', color='blue', linewidth=2)
plt.plot(x_eval, y_num_func, label='SciPy', color='red', linestyle='--', linewidth=2)
plt.title("Решения дифференциального уравнения на [0, 10]")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("solution_comparison.png", dpi=150)
plt.show()

plt.figure(figsize=(10, 5))
diff = y_sym_func(x_eval) - y_num_func
plt.plot(x_eval, diff, label='SymPy - SciPy', color='green', linewidth=2)
plt.title("Разность символьного и численного решений")
plt.xlabel("x")
plt.ylabel("Погрешность")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("solution_difference.png", dpi=150)
plt.show()