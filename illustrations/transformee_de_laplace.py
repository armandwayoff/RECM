import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

mpl.use("pgf")

c = 0

t = np.linspace(-1.5, 1, 1000)
heaviside_shifted = np.heaviside(t - c, 1)

s = np.linspace(0.01, 0.7, 1000) 
laplace_transform = np.exp(-c * s) / s

time_xticks = [c]
time_yticks = [0, 1]
time_xtick_labels = ["c"]
time_ytick_labels = [0, 1]  

laplace_xticks = [0]
laplace_xtick_labels = [f'{tick} units' for tick in laplace_xticks]  

plt.figure(figsize=(3, 6))

plt.subplot(2, 1, 1)
plt.plot(t, heaviside_shifted, label=r'$H(t - c)$')
# plt.title(r'Fonction échelon')
plt.xlabel('$t$')
plt.xticks(time_xticks, time_xtick_labels)  
plt.yticks(time_yticks, time_ytick_labels) 
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(s, laplace_transform, label=r'$\frac{\mathrm{e}^{-cp}}{p}$', color='orange')
# plt.title('$\text{Transformée de \textsc{Laplace}}$')
plt.xlabel('$p$')
plt.ylabel(r'$\mathcal{L}\{H(t - c)\}(p)$')
plt.xticks(laplace_xticks)
plt.yticks([0])
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

plt.savefig("transformee_de_laplace.pgf")
