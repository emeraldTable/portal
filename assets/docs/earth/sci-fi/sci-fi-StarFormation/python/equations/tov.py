import random
import math
import matplotlib.pyplot as plt


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

layer_radii = []
layer_pressures = []
layer_dP_dr = []

for i, layer in enumerate(cluster):
    print(f"\nLayer {i+1}:")
    print("Radius: {:.2f} meters".format(layer["Radius"]))
    print("Mass: {:.2f} kilograms".format(layer["Mass"]))
    print("Density: {:.2f} kg/m^3".format(layer["Density"]))
    print("Pressure: {:.2f} N/m^2".format(layer["Pressure"]))
    print("dP/dr: {:.2f} N/(m^2/m)".format(layer["dP/dr"]))

    layer_radii.append(layer["Radius"])
    layer_pressures.append(layer["Pressure"])
    layer_dP_dr.append(layer["dP/dr"])

# Plotting the data with equation information
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plotting Pressure vs Radius
ax1.plot(layer_radii, layer_pressures, 'bo-', label='Pressure')
ax1.set_xlabel('Radius (m)')
ax1.set_ylabel('Pressure (N/m^2)')
ax1.set_title('Pressure vs Radius')
ax1.legend()

# Add equation information
equation_text = r'$P = \frac{G(\rho + c^2(\frac{m}{4\pi r^3}))}{3(1 - \frac{2Gm}{r c^2 M})}$'
ax1.text(0.05, 0.95, equation_text, transform=ax1.transAxes, fontsize=12, verticalalignment='top')

# Add numerical results
for layer in cluster:
    radius = layer["Radius"]
    pressure = layer["Pressure"]
    equation_result = f'P = {pressure:.2f} N/m^2'
    ax1.text(radius, pressure, equation_result, fontsize=8, ha='center', va='bottom')

# Plotting dP/dr vs Radius
ax2.plot(layer_radii, layer_dP_dr, 'ro-', label='dP/dr')
ax2.set_xlabel('Radius (m)')
ax2.set_ylabel('dP/dr (N/(m^2/m))')
ax2.set_title('dP/dr vs Radius')
ax2.legend()

# Add equation information
equation_text = r'$\frac{{dP}}{{dr}} = -G(\rho + P)(m + \frac{4}{3}\pi r^3 P) / (r(r - \frac{2Gm}{c^2M}))$'
ax2.text(0.05, 0.95, equation_text, transform=ax2.transAxes, fontsize=12, verticalalignment='top')

# Add numerical results
for layer in cluster:
    radius = layer["Radius"]
    dP_dr = layer["dP/dr"]
    equation_result = f'dP/dr = {dP_dr:.2f} N/(m^2/m)'
    ax2.text(radius, dP_dr, equation_result, fontsize=8, ha='center', va='bottom')

plt.tight_layout()

# Saving the plot as a PNG image
plt.savefig('cluster_properties_lines.png')

# Lista de cores
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF']

# Plotting the data with circles
fig, ax = plt.subplots(figsize=(10, 8))

# Adicionar círculos representando cada camada
for i, layer in enumerate(cluster):
    radius = layer["Radius"]
    pressure = layer["Pressure"]
    color = colors[i % len(colors)]
    circle = plt.Circle((0, 0), radius, edgecolor='black', facecolor=color, alpha=0.66)
    ax.add_patch(circle)
    ax.annotate(f'P = {pressure:.2f} N/m^2', xy=(1.05, i), xycoords='data',
                fontsize=8, ha='left', va='center')

# Adicionar círculo central
central_radius = cluster[0]["Radius"]
central_circle = plt.Circle((0, 0), central_radius, edgecolor='black', facecolor='none', linewidth=4)
ax.add_patch(central_circle)

# Adicionar informações da equação
equation_text = r'$P = \frac{G(\rho + c^2(\frac{m}{4\pi r^3}))}{3(1 - \frac{2Gm}{r c^2 M})}$'
ax.text(0.5, 0.95, equation_text, transform=ax.transAxes, fontsize=12, ha='center', va='top')

# Definir proporção de aspecto como igual e ajustar limites do gráfico
ax.set_aspect('equal')
ax.autoscale()

# Remover eixos
ax.axis('off')

# Salvar resultado referente a cada círculo
result_text = ""
for i, layer in enumerate(cluster):
    radius = layer["Radius"]
    pressure = layer["Pressure"]
    result_text += f"Layer {i+1}: Radius = {radius:.2f} m, Pressure = {pressure:.2f} N/m^2\n"

# Exibir resultado ao lado da imagem
plt.text(1.1, 0.5, result_text, fontsize=10, ha='left', va='center')

# Salvar o gráfico como imagem PNG
plt.savefig('cluster_properties_circles.png', bbox_inches='tight', pad_inches=0.1)

# Display the plot
#plt.show()
