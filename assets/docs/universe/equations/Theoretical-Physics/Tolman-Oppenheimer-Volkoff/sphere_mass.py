import math

# Prompt the user for inputs
radius = float(input("Enter the radius of the sphere (in meters): "))
thickness = float(input("Enter the thickness of the sphere (in meters): "))
density = float(input("Enter the density of the alloy (in kg/m^3): "))

# Calculate the internal and external volumes
internal_volume = (4/3) * math.pi * radius**3
external_radius = radius + thickness
external_volume = (4/3) * math.pi * external_radius**3

# Calculate the volume of the shell
shell_volume = external_volume - internal_volume

# Calculate the total weight
total_weight = shell_volume * density

# Display the result
print("The total weight of the sphere is:", total_weight, "kg")
