import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

layer_names = ["Crust", "Upper Mantle", "Lower Mantle", "Outer Core", "Inner Core"]
layer_radii = [0, 40, 660, 2891, 5150, 6371]
layer_colors = ['red', 'orange', 'blue', 'green', 'yellow', 'purple']

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])

# Plotting the layers as colored sections of the sphere
for i in range(len(layer_radii) - 1):
    radius_inner = layer_radii[i]
    radius_outer = layer_radii[i + 1]
    color = layer_colors[i]

    # Create the theta and phi values for the surface
    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)

    # Parametric equations for a sphere
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    # Create a mask for the desired layers
    mask = np.logical_and(z >= -1, z <= 0)
    mask = np.logical_and(mask, radius_inner <= np.sqrt(x**2 + y**2 + z**2))
    mask = np.logical_and(mask, radius_outer >= np.sqrt(x**2 + y**2 + z**2))

    # Apply the mask to the surface coordinates
    x_masked = np.ma.masked_array(x * radius_outer, mask=~mask)
    y_masked = np.ma.masked_array(y * radius_outer, mask=~mask)
    z_masked = np.ma.masked_array(z * radius_outer, mask=~mask)

    # Plot the masked surface with the corresponding color
    ax.plot_surface(x_masked, y_masked, z_masked, color=color, alpha=0.8)

# Plotting the grid on the cube with colors corresponding to the layers
for i in range(len(layer_radii) - 1):
    radius_inner = layer_radii[i]
    radius_outer = layer_radii[i + 1]
    color = layer_colors[i]

    # Plotting the lines along X-axis
    ax.plot([-radius_outer, radius_outer], [-radius_outer, -radius_outer], [radius_inner, radius_inner], color=color)
    ax.plot([-radius_outer, radius_outer], [-radius_outer, -radius_outer], [-radius_inner, -radius_inner], color=color)
    ax.plot([-radius_outer, radius_outer], [radius_outer, radius_outer], [radius_inner, radius_inner], color=color)
    ax.plot([-radius_outer, radius_outer], [radius_outer, radius_outer], [-radius_inner, -radius_inner], color=color)

  # Plotting the lines along Y-axis
    ax.plot([-radius_outer, -radius_outer], [-radius_outer, radius_outer], [radius_inner, radius_inner], color=color)
    ax.plot([-radius_outer, -radius_outer], [-radius_outer, radius_outer], [-radius_inner, -radius_inner], color=color)
    ax.plot([radius_outer, radius_outer], [-radius_outer, radius_outer], [radius_inner, radius_inner], color=color)
    ax.plot([radius_outer, radius_outer], [-radius_outer, radius_outer], [-radius_inner, -radius_inner], color=color)

    # Plotting the lines along Z-axis
    ax.plot([-radius_outer, -radius_outer], [radius_inner, radius_inner], [-radius_outer, radius_outer], color=color)
    ax.plot([-radius_outer, -radius_outer], [-radius_inner, -radius_inner], [-radius_outer, radius_outer], color=color)
    ax.plot([radius_outer, radius_outer], [radius_inner, radius_inner], [-radius_outer, radius_outer], color=color)
    ax.plot([radius_outer, radius_outer], [-radius_inner, -radius_inner], [-radius_outer, radius_outer], color=color)


# Set axis labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Earth Layers")

# Set up the table with layer names and radii
table_data = [["Layer", "Radius (km)"]]
for i in range(len(layer_names)):
    table_data.append([layer_names[i], layer_radii[i]])

# Create a table at the top right corner of the plot
table = ax.table(cellText=table_data, loc='upper right', colWidths=[0.2, 0.2], cellLoc='center')

# Add the corresponding color to each layer in the table
for i in range(1, len(layer_names) + 1):
    table[i, 0].set_facecolor(layer_colors[i - 1])
    table[i, 0].set_edgecolor('black')

# Adjust the style of the table
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Save the figure as a PNG image
plt.savefig("earth_layers-deep.png")
