import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
def f(x):
    return (-3*(x-4.5)**2 + 60)

plt.plot(range(0, 2), [6]*2)
plt.plot(range(2, 8), [60]*6)
plt.plot(range(8, 10), [6]*2)
plt.plot(x, f(x))
plt.scatter(6, f(6), color="purple")
plt.show()