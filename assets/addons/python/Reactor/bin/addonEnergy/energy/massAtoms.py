# Atomic masses (in atomic mass units) of the elements
atomic_masses = {
    1: {'element': 'Hydrogen', 'mass': 1.008},
    2: {'element': 'Helium', 'mass': 4.0026},
    3: {'element': 'Deuterium', 'mass': 2.014},
    4: {'element': 'Tritium', 'mass': 3.016},
    5: {'element': 'Americium', 'mass': 243.061},
    6: {'element': 'Uranium', 'mass': 238.0289},
    7: {'element': 'Plutonium', 'mass': 244},
    8: {'element': 'Other', 'mass': 50.0}  # Placeholder value for other elements
}

# Avogadro's constant (atoms per mole)
avogadro_constant = 6.02214076e23

def calculate_atoms_per_kilogram(element, element_mass):
    # Calculate the number of atoms per kilogram
    atomic_mass = element['mass']
    moles = element_mass / atomic_mass
    atoms = moles * avogadro_constant
    atoms_per_kilogram = atoms / element_mass

    return atoms_per_kilogram

# Print the available elements and their corresponding numbers
print("Choose an element:")
for num, element in atomic_masses.items():
    print(f"{num}. {element['element']}")

# Take user input for the selected element and its mass
element_num = int(input("Enter the number of the element: "))
element_mass = float(input("Enter the mass of the element in kilograms: "))

# Retrieve the selected element from the atomic_masses dictionary
selected_element = atomic_masses.get(element_num, atomic_masses[8])  # Default to 'Other' if an invalid number is chosen

# Calculate the number of atoms per kilogram for the selected element
atoms_per_kg = calculate_atoms_per_kilogram(selected_element, element_mass)

# Calculate the total number of atoms based on the chosen element's mass
total_atoms = atoms_per_kg * element_mass

# Print the results
print(f"Atoms per kilogram of {selected_element['element']}: {atoms_per_kg}")
print(f"Total number of atoms for {selected_element['element']} with mass {element_mass} kg: {total_atoms}")

