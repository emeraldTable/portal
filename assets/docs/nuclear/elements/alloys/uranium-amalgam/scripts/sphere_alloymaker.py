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

    return volume_uranium, volume_mercury

# User input
thickness = float(input("Enter the thickness of the sphere in centimeters: "))
radius = float(input("Enter the radius of the sphere in meters: "))

# Calculate the amount of uranium and mercury
uranium, mercury = calculate_amalgam_amount(thickness, radius)

# Print the results
print(f"Amount of uranium: {uranium} cubic meters")
print(f"Amount of mercury: {mercury} cubic meters")
