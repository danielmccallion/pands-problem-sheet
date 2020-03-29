# Daniel Mc Callion
# This program displays a plot of the functions f(x)=x, g(x)=x**2 and h(x)=x**3
# in the range [0, 4] on the one set of axes. 

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 4.0, 100)

g = x**2
h = x**3

plt.plot(x, x, "r.", label=r"$f(x) = x$")
plt.plot(x, g, "g.", label=r"$g(x) = x^2$")
plt.plot(x, h, "b.", label=r"$h(x) = x^3$")

plt.legend()
plt.title("f(x) vs. g(x) vs. h(x)", fontsize=18)
plt.xlabel("x value", fontsize=14)
plt.ylabel("Result", fontsize=14)
plt.grid(True)
plt.show()
