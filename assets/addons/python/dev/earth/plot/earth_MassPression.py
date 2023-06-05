import numpy as np
import matplotlib.pyplot as plt

# Constants
Earth_Radius = 6371  # km
Density = 5515  # kg/m^3

# Calculations
radius = np.linspace(0, Earth_Radius, 1000)  # Generating 1000 points from 0 to Earth's radius
volume = (4/3) * np.pi * radius**3
mass = Density * volume
pressure = (2/3) * np.pi * Density * radius**2

# Creating the plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(radius, mass, label='Mass')
ax.plot(radius, pressure, label='Pressure')

# Setting up the plot
ax.set_xlabel('Radius (km)')
ax.set_ylabel('Value')
ax.set_title('Distribution of Mass and Pressure')
ax.legend()

# Printing the results near the legend
mass_label = f"Mass: {int(mass[-1]):,} kg"
pressure_label = f"Pressure: {int(pressure[-1]):,} N/m^2"
ax.annotate(mass_label, xy=(Earth_Radius, mass[-1]), xytext=(Earth_Radius + 100, mass[-1]), fontsize=12,
            arrowprops=dict(facecolor='black', arrowstyle='->'))
ax.annotate(pressure_label, xy=(Earth_Radius, pressure[-1]), xytext=(Earth_Radius + 100, pressure[-1]), fontsize=12,
            arrowprops=dict(facecolor='black', arrowstyle='->'))

# Printing the constants in a box
constants_box = f"Earth Radius: {Earth_Radius} km\nDensity: {Density} kg/m^3"
ax.text(0.15, 0.98, constants_box, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Saving the plot as PNG
plt.savefig('mass_pressure_graph.png', bbox_inches='tight')
plt.show()
