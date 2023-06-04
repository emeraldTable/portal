import matplotlib.pyplot as plt

layer_names = ["Crust", "Upper Mantle", "Lower Mantle", "Outer Core", "Inner Core"]
layer_radii = [6371, 5771, 3480, 1221, 637]

# Plotting the Earth layers
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')

colors = ['#f4d03f', '#27ae60', '#3498db', '#f39c12', '#e74c3c']

for i, radius in enumerate(layer_radii):
    ax.add_patch(plt.Circle((0, 0), radius, color=colors[i]))

ax.set_xlim(-6500, 6500)
ax.set_ylim(-6500, 6500)
ax.axis('off')

# Displaying the radius values
for i, radius in enumerate(layer_radii):
    ax.text(0, -radius - 100, f"{layer_names[i]}\n{radius} km", ha='center', fontsize=10)

# Save the image as a PNG file  
plt.savefig('earth_layers.png', dpi=300)
