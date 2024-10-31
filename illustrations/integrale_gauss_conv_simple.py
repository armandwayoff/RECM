import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams['text.usetex'] = True

mpl.use("pgf")

a = 2.5
n_values = [1, 2, 3, 5, 10]
x = np.linspace(0, a, 1000)

plt.figure(figsize=(3, 2.5))
num_curves = len(n_values)
cmap = plt.get_cmap("Blues")

for i, n in enumerate(n_values):
    fn = np.where(x < np.sqrt(n), (1 - (x**2) / n)**n, 0)
    plt.plot(x, fn, label=f"$n={n}$", color=cmap((i + 2) / num_curves), linewidth=1.5)

plt.plot(x, np.exp(-x**2), 'r', label="$t \mapsto \mathrm{e}^{-t^2}$", linewidth=1.5)

plt.xlabel("$t$")
plt.xticks([0], ['$0$'])
plt.yticks([0, 1], ['$0$', '$1$'])
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.savefig("integrale_gauss_conv_simple.pgf")
