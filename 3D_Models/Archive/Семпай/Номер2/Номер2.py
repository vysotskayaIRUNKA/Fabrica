import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def read_system(path):
    with open(path, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])
    A = np.array([list(map(float, lines[i].split())) for i in range(1, n + 1)])
    b = np.array(list(map(float, lines[n + 1].split())))
    return A, b, n


def solve_and_save(path, out_png):
    A, b, n = read_system(path)
    x = np.linalg.solve(A, b)
    print(f"--- {path} (N={n}) ---")
    print("x =", x)
    print("residual =", np.linalg.norm(A @ x - b))
    print()

    plt.figure(figsize=(14, 6))
    plt.bar(np.arange(n), x, width=0.8, color="steelblue")
    plt.grid(True, zorder=0)
    plt.xticks(np.arange(0, n, max(1, n // 20)))
    plt.xlabel("i")
    plt.ylabel("x[i]")
    plt.title(f"x для {Path(path).name} (N={n})")
    plt.tight_layout()
    plt.savefig(out_png, dpi=150)
    plt.close()
    print(f"Сохранено: {out_png}\n")


solve_and_save("TestMatrix.txt", "test_plot.png")
solve_and_save("RealMatrix.txt", "real_plot.png")