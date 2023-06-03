import numpy as np
import matplotlib.pyplot as plt

# Define the goal position
goal = np.array([5, 5])

# Define the obstacle positions
obstacles = np.array([[3, 4], [7, 6], [4, 8]])

# Define parameters for attractive and repulsive forces
attractive_gain = 0.5
repulsive_gain = 10.0
repulsive_radius = 2.0

def calculate_attractive_force(position):
    attractive_force = attractive_gain * (goal - position)
    return attractive_force

def calculate_repulsive_force(position):
    repulsive_force = np.zeros(2)
    for obstacle in obstacles:
        distance = np.linalg.norm(position - obstacle)
        if distance <= repulsive_radius:
            direction = (position - obstacle) / distance
            repulsive_force += repulsive_gain * ((1 / distance) - (1 / repulsive_radius)) * (1 / distance**2) * direction
    return repulsive_force

def calculate_resultant_force(position):
    attractive_force = calculate_attractive_force(position)
    repulsive_force = calculate_repulsive_force(position)
    resultant_force = attractive_force + repulsive_force
    return resultant_force

# Generate a grid of points
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
grid_points = np.vstack((X.flatten(), Y.flatten())).T

# Calculate the potential field at each point
potential_field = np.zeros(len(grid_points))
for i, point in enumerate(grid_points):
    potential_field[i] = np.linalg.norm(calculate_resultant_force(point))

# Reshape the potential field for plotting
potential_field = potential_field.reshape(X.shape)

# Plot the potential field
plt.contourf(X, Y, potential_field, cmap='jet')
plt.colorbar(label='Potential Field')
plt.plot(goal[0], goal[1], 'ro', label='Goal')
plt.plot(obstacles[:, 0], obstacles[:, 1], 'ks', label='Obstacles')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Potential Field')
plt.legend()
plt.axis('equal')
plt.show()

