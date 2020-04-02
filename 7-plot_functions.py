# Daniel Mc Callion
# This program displays a plot of the functions f(x)=x, g(x)=x**2 and h(x)=x**3
# in the range [0, 4] on the one set of axes. 

# Libaries matplotlib for plotting the graphs and numpy for generating a numbers for the functions
import matplotlib.pyplot as plt
import numpy as np

# Using linspace from numpy to generate a list of 100 values evenly spaced bewteen 0 and 4 
x = np.linspace(0.0, 4.0, 100)

# g is the function g(x) where x gets squared
g = x**2
# h is the function h(x) where x gets cubed
h = x**3

# Create the plot for f(x) which is just x, use Mathtext label to style the label in italic 
plt.plot(x, x, "r.", label=r"$f(x) = x$")
# Create the plot for g(x) which is x to the power of 2
# Use Mathtext label to style the label in italic and to get a superscript 2
plt.plot(x, g, "g.", label=r"$g(x) = x^2$")
# Create the plot for h(x) which is x to the power of 3
# Use Mathtext label to style the label in italic and to get a superscript 3
plt.plot(x, h, "b.", label=r"$h(x) = x^3$")

# Add the legend to the graph
plt.legend()
# Add a title to the graph with the font size large as its the title
plt.title("f(x) vs. g(x) vs. h(x)", fontsize=18)
# Label for the x axis with a slightly larger than standard font for clarity 
plt.xlabel("x value", fontsize=14)
# Label for the y axis with a slightly larger than standard font for clarity 
plt.ylabel("Result", fontsize=14)
# Added a grid to the graph for reading values easier
plt.grid(True)
# Show the final graph to the user 
plt.show()
