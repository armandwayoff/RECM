import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

X = np.arange(0, 7, 0.001)

g = lambda x: x**(1/2) + 2 * x**2 - np.log(x + 1) + 2

K = [1, 5, 50, 100]


fig, ax = plt.subplots(len(K), 1, constrained_layout=True)
for i, k in enumerate([1, 5, 50, 100]):
    f = lambda x: np.sin(k * x) * g(x)
    f = np.vectorize(f)
    I = integrate.quad(f, 0, 2*np.pi)[0]
    lab = "{k}, {I:.2f}".format(k=k, I=I)
    ax[i].set_title(r"$x \mapsto \sin($"+str(k)+r"$\cdot x) f(x)$")
    ax[i].plot(X, f(X), label=lab)

plt.savefig("integration-02_lebesgue.png")
