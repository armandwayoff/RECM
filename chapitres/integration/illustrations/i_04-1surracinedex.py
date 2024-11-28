import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x):
    return 1 / np.sqrt(x)

a, b = 0.01, 1 
n = 10  # Nombre de sous-intervalles
dx = (b - a) / n  

x_left = np.linspace(a, b - dx, n)
riemann_sum = np.sum(f(x_left) * dx)

mpl.use("pgf")

fig, ax = plt.subplots(figsize=(3, 3))

x = np.linspace(a, b, 1000)
plt.plot(x, f(x), 'b-', label=r'$f(x) = \frac{1}{\sqrt{x}}$')

for i in range(n):
    xi = x_left[i]
    plt.bar(xi, f(xi), width=dx, align='edge', color='teal', alpha=0.5, edgecolor='black')

x_ticks = [0, 0.25, 0.5, 0.75, 1]
x_labels = ['$0$', '$1/4$', '$1/2$', '$3/4$', '$1$']  
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels)

y_ticks = [0, 5, 10]
y_labels = ['$0$', '$5$', '$10$']  
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

plt.savefig("1surracinedex.pgf")



