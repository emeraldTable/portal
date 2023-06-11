import math
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np  # Import the numpy module and give it an alias of np

atomic_masses = {
    "plutonium": 244,
    "uranium": 238,
    "curium": 247,
    "neptunium": 237,
    "americium": 243,
    "berkelium": 247,
    "californium": 251,
    "thorium": 232,
    "protactinium": 231,
    "actinium": 227,
    "thallium": 208,
    "rhenium": 186,
    "promethium": 145,
    "terbium": 158,
    "europium": 152,
    "holmium": 164,
    "ytterbium": 173,
    "lutetium": 175,
    "einsteinium": 252,
    "fermium": 257,
    "mendelevium": 258,
    "nobelium": 259,
    "lawrencium": 266,
    "rutherfordium": 267,
    "DeFi": 314
}

def calculate_properties(r, m, element):
    G = 6.67430e-11  # Gravitational constant in m^3/(kg·s^2)
    c = 299792458  # Speed of light in vacuum in m/s
    v = (4/3) * math.pi * r**3
    ρ = m / v
    atomic_mass = atomic_masses[element]
    P = (G * (ρ + c**2 * (m / (4*math.pi*r**3)))) / (3 * (1 - (2 * G * m) / (r * c**2 * atomic_mass)))
    dP_dr = - G * (ρ + P) * (m + (4/3) * math.pi * r**3 * P) / (r * (r - (2 * G * m) / (c**2 * atomic_mass)))
    return ρ, P, dP_dr

def create_cluster():
    num_layers = int(input("Enter the number of layers in the cluster: "))
    cluster = []
    for i in range(num_layers):
        print(f"\nLayer {i+1}:")
        radius_unit = input("Choose the unit of measurement for the radius (1 for m, 2 for cm, 3 for mm): ")
        radius_option = int(radius_unit)
        radius = float(input("Enter the radius: "))
        mass_unit = input("Choose the mass unit (1 for t, 2 for kg, 3 for g, 4 for mg): ")
        mass_option = int(mass_unit)
        mass = float(input("Enter the mass: "))
        element = input("Choose the element (plutonium, uranium, curium): ")
        
        # Conversion of units to meters and kilograms
        if radius_option == 2:
            radius /= 100.0
        elif radius_option == 3:
            radius /= 1000.0
        if mass_option == 1:
            mass *= 1000.0
        elif mass_option == 3:
            mass /= 1000.0
        elif mass_option == 4:
            mass /= 1000000.0
        
        density, pressure, dP_dr = calculate_properties(radius, mass, element)
        layer = {"Radius": radius, "Mass": mass, "Density": density, "Pressure": pressure, "dP/dr": dP_dr}
        cluster.append(layer)
    
    return cluster

# Create the cluster
cluster = create_cluster()

# Display the properties of each layer
print("\nCluster Properties:")
for i, layer in enumerate(cluster):
    print(f"\nLayer {i+1}:")
    print("Radius: {:.2f} meters".format(layer["Radius"]))
    print("Mass: {:.2f} kilograms".format(layer["Mass"]))
    print("Density: {:.2f} kg/m^3".format(layer["Density"]))
    print("Pressure: {:.2f} N/m^2".format(layer["Pressure"]))
    print("dP/dr: {:.2f} N/(m^2/m)".format(layer["dP/dr"]))

# Define the colormap for the outer spheres (grayscale)
gray_cmap = LinearSegmentedColormap.from_list("gray_cmap", [(0, "gray"), (1, "gray")])

# Create the 3D plot of the cluster
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add the layers to the plot
for i, layer in enumerate(cluster):
    r = layer["Radius"]
    density = layer["Density"]
    
    if i == 0:
        color = 'red'  # Innermost sphere is red
        alpha = 0.7  # No transparency for innermost sphere
    else:
        # Grayscale color based on density
        color = gray_cmap((density - min([l["Density"] for l in cluster])) / (max([l["Density"] for l in cluster]) - min([l["Density"] for l in cluster])))
        alpha = 0.3  # Complete transparency for outer spheres
    
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = r * np.cos(u) * np.sin(v)
    y = r * np.sin(u) * np.sin(v)
    z = r * np.cos(v)
    ax.plot_surface(x, y, z, color=color, alpha=alpha, edgecolor='none')

# Add smaller clusters inside the larger ones
if i < len(cluster) - 1:
    r1 = layer["Radius"]
    r2 = cluster[i+1]["Radius"]
    x1, y1, z1 = np.mgrid[-r1:r1:2*r2*1j, -r1:r1:2*r2*1j, -r1:r1:2*r2*1j]
    inside = (x1**2 + y1**2 + z1**2) < r2**2
    x2, y2, z2 = np.broadcast_to(np.array([x[i], y[i], z[i]]), x1.shape)
    facecolors = np.broadcast_to(np.array([(color, 0, 1-color)]), x1.shape + (3,))
    ax.voxels(x2, y2, z2, inside, facecolors=facecolors, edgecolor='k', alpha=0.2)

# Set the limits of the plot
max_radius = max([l["Radius"] for l in cluster])
ax.set_xlim([-max_radius, max_radius])
ax.set_ylim([-max_radius, max_radius])
ax.set_zlim([-max_radius, max_radius])

# Add labels to the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Save the image in .png format
plt.savefig("cluster.png")
