import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

mpl.use("pgf")

def F(x):
    result, _ = quad(lambda t: np.exp(-t) / t, x, np.inf)
    return result

def F1(x):
    return np.exp(-x) / x + np.exp(-x) / (x**2)

x_values = np.linspace(0.0001, 0.5, 300) # 10, 18
F_values = [F(x) for x in x_values]
F1_values = [F1(x) for x in x_values]
F2_values = [-np.log(x) for x in x_values]

fig, ax = plt.subplots(figsize=(3, 3)) 
plt.plot(x_values, F_values, label='$F(x) = \int_x^{+\infty} \\frac{\mathrm{e}^{-t}}{t} \\, \mathrm{d} t$', color='blue')
# plt.plot(x_values, F1_values, label='$x \mapsto \\frac{\mathrm{e}^{-x}}{x} + \\frac{\mathrm{e}^{-x}}{x^2}$', color='red')
plt.plot(x_values, F2_values, label='$x \mapsto -\ln(x)$', color='green')

plt.xlabel("$x$")
# plt.ylabel("$f(x)$")
plt.grid(True)

x_ticks = [0]
x_labels = ['$0$']  
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels)

y_ticks = []
y_labels = []  
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

plt.legend()
plt.tight_layout()
plt.show()

plt.savefig("un_developpement_asymptotique_en0.pgf")
