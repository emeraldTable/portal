def calculate_component_masses(uranium_mass):
    # Calculate the masses of hydrogen and helium
    hydrogen_mass = 0.75 * uranium_mass
    helium_mass = 0.25 * uranium_mass

    return hydrogen_mass, helium_mass


# Take user input for the mass of uranium
uranium_input = input("Enter the mass of uranium in kilograms: ")
uranium_mass = float(uranium_input)

# Call the function to calculate the component masses
hydrogen_mass, helium_mass = calculate_component_masses(uranium_mass)

# Print the results
print("Mass of Hydrogen: ", hydrogen_mass, "kg")
print("Mass of Helium: ", helium_mass, "kg")
print("Mass of Uranium: ", uranium_mass, "kg")
