# Constants
uranium_to_hydrogen_ratio = 500   # Hydrogen atoms per uranium atom
avogadro_number = 6.02214076e23  # Avogadro's number (atoms/mol)

# Function to calculate the total number of hydrogen atoms
def calculate_hydrogen_atoms(uranium_weight):
    # Convert uranium weight to moles
    uranium_moles = uranium_weight / 238.02891   # Molar mass of uranium-238

    # Calculate the total number of uranium atoms
    uranium_atoms = uranium_moles * avogadro_number

    # Calculate the total number of hydrogen atoms
    hydrogen_atoms = uranium_atoms * uranium_to_hydrogen_ratio

    return hydrogen_atoms

# Prompting the user for input
uranium_weight = float(input("Enter the weight of uranium (in kg): "))

# Calling the function to calculate the total number of hydrogen atoms
total_hydrogen_atoms = calculate_hydrogen_atoms(uranium_weight)

# Displaying the result
print(f"The total number of hydrogen atoms required is approximately {total_hydrogen_atoms:.2e}.")

