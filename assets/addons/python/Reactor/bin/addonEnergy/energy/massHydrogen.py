def calculate_hydrogen_mass(megatons):
    # Conversion factor from megatons to joules
    megaton_to_joules = 4.184e15

    # Energy calculation
    energy = megatons * megaton_to_joules

    # Speed of light
    speed_of_light = 3.0e8

    # Mass calculation using E = mc^2
    mass = energy / speed_of_light**2

    return mass

# Prompting the user for input
megatons = float(input("Enter the energy in megatons: "))

# Calling the function to calculate the hydrogen mass
hydrogen_mass = calculate_hydrogen_mass(megatons)

# Displaying the result
print(f"The required hydrogen mass is approximately {hydrogen_mass:.3f} kilograms.")

