import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

X = np.arange(0, 7, 0.005)

g = lambda x: x**(1/2) + 2 * x**2 - np.log(x + 1) + 2

K = [1, 5, 50] # 100

fig, ax = plt.subplots(len(K), 1, constrained_layout=True, figsize=(3, 6))
for i, k in enumerate(K):
    f = lambda x: np.sin(k * x) * g(x)
    f = np.vectorize(f)
    Y = f(X)
    positive_area = np.where(Y > 0, Y, 0)
    negative_area = np.where(Y < 0, Y, 0)
    I = integrate.quad(f, 0, 2*np.pi)[0]
    lab = "{k}, {I:.2f}".format(k=k, I=I)
    if k == 1:
        ax[i].set_title(r"$x \mapsto \sin(x) f(x)$")
    else:
        ax[i].set_title(r"$x \mapsto \sin(" + str(k) + r"\,x) f(x)$")
    ax[i].plot(X, Y, label=lab, linewidth=0.5)
    ax[i].plot(X, g(X), '--r', label=lab, linewidth=0.5)
    ax[i].plot(X, -g(X), '--r', label=lab, linewidth=0.5)
    ax[i].fill_between(X, positive_area, color='blue', alpha=0.3)
    ax[i].fill_between(X, negative_area, color='red', alpha=0.3)
    # plt.axes([0, max(X), -max(g(X)), max(g(X))]) 

# plt.show()

plt.savefig("integration-02_lebesgue.png", dpi=300)