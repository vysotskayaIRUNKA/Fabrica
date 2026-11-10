import sympy as sp

lam, mu, rho = sp.symbols('lambda mu rho')

M = sp.Matrix([
    [0, 0, 0, -1/rho, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1/rho, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1/rho, 0, 0, 0],
    [-(lam + 2*mu), 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -mu, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -mu, 0, 0, 0, 0, 0, 0],
    [-lam, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-lam, 0, 0, 0, 0, 0, 0, 0, 0]
])

eigenvalues = M.eigenvals()

print("Собственные значения и их кратности:")
for val, mult in eigenvalues.items():
    print(f"Собственное значение: {val}, Кратность: {mult}")