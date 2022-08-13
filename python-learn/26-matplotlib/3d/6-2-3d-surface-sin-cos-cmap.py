import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Single Points
ax = plt.axes(projection="3d")

x_data = np.arange(-5, 5, 0.1)
y_data = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(x_data, y_data)
Z = np.sin(X) * np.cos(Y) 

ax.plot_surface(X, Y, Z, cmap="plasma")
ax.set_title("The Function")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
