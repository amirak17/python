import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import random

x_values = []
y_values = []

for i in range(1000):
	x_values.append(random.randint(0, 100))
	y_values.append(random.randint(0, 100))

	if i % 5 == 0:
		plt.xlim(0, 100)
		plt.ylim(0, 100)
		plt.scatter(x_values, y_values, color='black')
		plt.pause(0.0001)

plt.show()

# https://www.youtube.com/watch?v=7RgoHTMbp4A