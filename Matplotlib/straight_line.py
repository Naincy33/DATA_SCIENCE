import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

plt.plot(x, 2*x + 3, label="y = 2x + 3")
plt.plot(x, 2*x - 3, label="y = 2x - 3")
plt.plot(x, -2*x + 3, label="y = -2x + 3")
plt.plot(x, -2*x - 3, label="y = -2x - 3")

plt.axhline(0)
plt.axvline(0)

plt.legend()
plt.grid()
plt.show()