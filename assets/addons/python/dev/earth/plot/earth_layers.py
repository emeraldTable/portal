import matplotlib.pyplot as plt

# Properties of Earth layers (pressure in GPa and density in g/cm^3)
layers = [
    {"name": "Crust", "pressure": 0.1, "density": 2.7},
    {"name": "Upper Mantle", "pressure": 50, "density": 4.5},
    {"name": "Lower Mantle", "pressure": 140, "density": 5.5},
    {"name": "Outer Core", "pressure": 330, "density": 9.9},
    {"name": "Inner Core", "pressure": 360, "density": 13.1}
]

# Get data from the layers
names = [layer["name"] for layer in layers]
pressures = [layer["pressure"] for layer in layers]
densities = [layer["density"] for layer in layers]

# Plotting the data
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the pressure
ax.plot(names, pressures, 'b-o')
ax.set_ylabel('Pressure (GPa)', color='b')
ax.tick_params('y', colors='b')

# Plot the density
ax2 = ax.twinx()
ax2.plot(names, densities, 'r-o')
ax2.set_ylabel('Density (g/cm^3)', color='r')
ax2.tick_params('y', colors='r')

# Adjust x-axis labels
plt.xticks(rotation=45, ha='right')

# Set axes labels and title
ax.set_xlabel('Earth Layers')
ax.set_ylim(0, max(pressures) * 1.1)
ax2.set_ylim(0, max(densities) * 1.1)
plt.title('Properties of Earth Layers')

# Create a table with the results
table_data = []
for layer in layers:
    table_data.append([layer["name"], layer["pressure"], layer["density"]])

table = ax.table(cellText=table_data, colLabels=["Layer", "Pressure (GPa)", "Density (g/cm^3)"],
                 loc="lower right", bbox=[0.6, 0.1, 0.40, 0.41])

table.auto_set_font_size(False)
table.set_fontsize(8)

# Save the figure as a PNG file
plt.savefig('earth_layers_properties.png', dpi=300)
