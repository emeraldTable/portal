import matplotlib.pyplot as plt
import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
M = 5.972e24  # Mass of Earth (kg)
R = 6371000  # Radius of Earth (m)

# Function to calculate the gravitational acceleration at a given point
def gravitational_acceleration(x, y):
    r = np.sqrt(x**2 + y**2)
    r[r < R] = R  # Set distances within Earth's radius to Earth's radius to avoid division by zero
    return (G * M) / r**2

# Create a grid of points in the x-y plane
x = np.linspace(-10*R, 10*R, 1000)
y = np.linspace(-10*R, 10*R, 1000)
X, Y = np.meshgrid(x, y)

# Calculate the gravitational acceleration at each point in the grid
Z = gravitational_acceleration(X, Y)

# Plot the gravitational zone
plt.figure(figsize=(10, 10))
plt.contourf(X, Y, Z, cmap='Blues')
plt.colorbar(label='Gravitational Acceleration (m/s^2)')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Gravitational Zone around Earth')
plt.gca().set_aspect('equal')
plt.savefig('gravitational_accelerationzone.png')
plt.show()
