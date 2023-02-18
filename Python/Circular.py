# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 20:58:38 2023

@author: Gbenga Agunbiade
"""

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Reads the number of points from the user
N = int(input("Identify the number of sampled points: "))
# The x, y, x components of the points as arrays of uniform random numbers
x = np.random.rand(1,N)
y = np.random.rand(1,N)
z = np.random.rand(1,N)
    # Evaluate the spherical shell condition for each point
xa, ya, za = [], [], []  # arrays for points that pass the condition
xm, ym, zm = [], [], []  # arrays for points that don't pass the condition

for i in range(0,N):
        k_squared = x[0,i]**2 + y[0,i]**2 + z[0,i]**2
        if 0.4 < k_squared < 0.95:
            xa.append(x[0,i])
            ya.append(y[0,i])
            za.append(z[0,i])
        else:
            xm.append(x[0,i])
            ym.append(y[0,i])
            zm.append(z[0,i])

print("The efficiency was: ", len(xa)/N)

fig = plt.figure()

# Create a 3D subplot in the second position
ax2 = fig.add_subplot(111, projection='3d')
ax2.scatter(xa, ya, za, c="r")
ax2.scatter(xm, ym, zm, c="b")
ax2.set_title("3D Plot")

plt.show()
