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

from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
M = 5.972e24  # Mass of Earth (kg)
R = 6371000  # Radius of Earth (m)

# Function to calculate the gravitational acceleration at a given point
def gravitational_accelerationKM(x, y):
    r = np.sqrt(x**2 + y**2)
    r[r < R] = R  # Set distances within Earth's radius to Earth's radius to avoid division by zero
    return (G * M) / r**2

# Create a grid of points in the x-y plane
x = np.linspace(-10*R, 10*R, 1000)
y = np.linspace(-10*R, 10*R, 1000)
X, Y = np.meshgrid(x, y)

# Calculate the gravitational acceleration at each point in the grid
Z = gravitational_accelerationKM(X, Y)

# Plot the gravitational zone
fig, ax = plt.subplots(figsize=(12, 10))
im = ax.contourf(X, Y, Z, cmap='Blues')
plt.colorbar(im, label='Gravitational Acceleration (m/s^2)')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Gravitational Zone around Earth')
ax.set_aspect('equal')


# Convert gravitational acceleration to velocity in kilometers per hour
velocity = np.sqrt(2 * Z) * 3.6

# Plot the gravitational zone with a blank space on the right
fig, ax = plt.subplots(figsize=(12, 10))
im = ax.contourf(X, Y, velocity, cmap='Blues')
plt.colorbar(im, label='Velocity (km/h)')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Gravitational Zone around Earth')
ax.set_aspect('equal')

# Create a blank space on the right
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
cax.axis('off')

# Add text annotations with the numerical values (converted to km/h)
for i in range(5):
    value = im.cvalues[i]  # Get the contour values from the image
    value_km_per_hr = np.sqrt(2 * value) * 3.6
    cax.text(0.5, (i + 0.5) / 5.0, f'{value_km_per_hr:.2f}', ha='center', va='center')

plt.savefig('gravitational_accelerationzone-KM.png')
