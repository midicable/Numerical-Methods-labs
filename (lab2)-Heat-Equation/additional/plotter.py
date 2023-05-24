import matplotlib.pyplot as plt
import numpy as np

def plot(u):
    x = np.linspace(0, 1, 21)
    t = np.linspace(0, 1, 401)
    X, T = np.meshgrid(x, t)
    Z = np.array(u)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, Z)

    plt.show()
