import math

def calculate_amalgam_amount(thickness_cm, radius_m):
    # Convert thickness to meters
    thickness_m = thickness_cm / 100

    # Calculate the volume of the entire sphere
    volume_sphere = (4/3) * math.pi * radius_m**3

    # Calculate the internal radius
    internal_radius = radius_m - thickness_m

    # Calculate the volume of the solid sphere
    volume_solid_sphere = (4/3) * math.pi * internal_radius**3

    # Calculate the volume of uranium and mercury
    volume_uranium = 0.8 * volume_solid_sphere
    volume_mercury = 0.2 * volume_solid_sphere

    # Calculate the density of the uranium amalgam
    mass_uranium = volume_uranium * 19050  # Assuming uranium density of 19,050 kg/m³
    mass_mercury = volume_mercury * 13534  # Assuming mercury density of 13,534 kg/m³
    total_mass = mass_uranium + mass_mercury
    density = total_mass / (volume_uranium + volume_mercury)

    return volume_uranium, volume_mercury, density

# User input
thickness = float(input("Enter the thickness of the sphere in centimeters: "))
radius = float(input("Enter the radius of the sphere in meters: "))

# Calculate the amount of uranium, mercury, and density
uranium, mercury, density = calculate_amalgam_amount(thickness, radius)

# Print the results
print(f"Amount of uranium: {uranium} cubic meters")
print(f"Amount of mercury: {mercury} cubic meters")
print(f"Density of the uranium amalgam: {density} kg/m³")
