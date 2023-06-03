import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Generate random points
np.random.seed(23)
points = np.random.rand(4, 2)

# Compute Voronoi diagram
vor = Voronoi(points)

# Plotting the Voronoi diagram
fig = voronoi_plot_2d(vor)
plt.plot(points[:, 0], points[:, 1], 'ko')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Voronoi Diagram')
plt.axis('equal')
plt.show()

