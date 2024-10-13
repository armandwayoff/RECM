import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(t):
    return 1 / (t * np.sqrt(t**2 - 1))

integral_value, _ = quad(f, 1, np.inf)

def Sn(n, max_k=10000):
    k_values = np.arange(n + 1, max_k + 1)
    terms = 1 / (k_values * np.sqrt(k_values**2 - n**2))
    return np.sum(terms)

n_values = np.array([1, 3, 6] + [k for k in range(10, 100, 10)])
Sn_values = np.array([n * Sn(n) for n in n_values])

mpl.use("pgf")

plt.figure(figsize=(3, 3))
plt.plot(n_values, Sn_values, label=r'$n S_n$', marker='o')
plt.axhline(y=integral_value, color='r', linestyle='--', label=r'$\int_{1}^{+\infty} f(t) \, \mathrm{d}t$')

plt.xlabel(r'$n$')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

plt.savefig("exo1-4-3.pgf")
