import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

# Generate random points
np.random.seed(0)
points = np.random.rand(30, 2)

# Perform Delaunay triangulation
tri = Delaunay(points)

# Plotting the triangulation
plt.triplot(points[:, 0], points[:, 1], tri.simplices)
plt.plot(points[:, 0], points[:, 1], 'o')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Delaunay Triangulation')
plt.axis('equal')
plt.show()

