import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Single Points
ax = plt.axes(projection="3d")

x_data = np.arange(0, 50, 0.1)
y_data = np.arange(0, 50, 0.1)
z_data = x_data * y_data

# ax.scatter(x_data, y_data, z_data, marker="v", alpha=0.8)
ax.plot(x_data, y_data, z_data)
plt.show()
