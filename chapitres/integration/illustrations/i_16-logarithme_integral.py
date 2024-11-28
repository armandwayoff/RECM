import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

mpl.use("pgf")

def integrande(t):
    return 1 / np.log(t)

def integrale(x):
    if x <= 0 or x >= 1:
        return np.nan  
    result, _ = quad(integrande, x, x**2)
    return result

x = np.linspace(0.001, 0.999, 500)
y = np.array([integrale(xi) for xi in x])

fig, ax = plt.subplots(figsize=(3, 2))

plt.plot(x, y, color='b')
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.grid(True)

x_ticks = [0, 0.25, 0.5, 0.75, 1]
x_labels = ['$0$', '$1/4$', '$1/2$', '$3/4$', '$1$']  
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels)

y_ticks = [0, 0.2, 0.4, 0.6]
y_labels = ['$0$', '$0{,}2$', '$0{,}4$', '$0{,}6$']  
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

plt.tight_layout()
plt.show()

plt.savefig("logarithme_integral.pgf")