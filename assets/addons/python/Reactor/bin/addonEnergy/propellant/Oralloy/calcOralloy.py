# Function to calculate the amount of Oralloy required
def calculate_oralloy_amount(oralloy_percentage, uranium_mass):
    oralloy_amount = oralloy_percentage * uranium_mass
    return oralloy_amount

# Defining the Oralloy types and their specifications
oralloy_types = {
    1: {
        'name': 'Oralloy-1',
        'percentage': 0.9315  # Oralloy-1 (93.15% U-235)
    },
    2: {
        'name': 'Oralloy-2',
        'percentage': 0.9515  # Oralloy-2 (95.15% U-235)
    },
    3: {
        'name': 'Oralloy-3',
        'percentage': 0.9625  # Oralloy-3 (96.25% U-235)
    }
}

# Printing the specifications of each Oralloy type
print("Oralloy Types and Specifications:")
for oralloy_type, specs in oralloy_types.items():
    print(f"{oralloy_type}. {specs['name']}: {specs['percentage']*100:.2f}% U-235")

# Prompting the user for input
oralloy_type = int(input("Choose the Oralloy type (1, 2, or 3): "))
uranium_mass_1 = float(input("Enter the mass of the first uranium sample (in kg): "))
uranium_mass_2 = float(input("Enter the mass of the second uranium sample (in kg): "))

# Checking if the selected Oralloy type is valid
if oralloy_type not in oralloy_types:
    print("Invalid Oralloy type selected!")
else:
    # Calculating the amount of Oralloy required for each uranium mass
    oralloy_amount_1 = calculate_oralloy_amount(oralloy_types[oralloy_type]['percentage'], uranium_mass_1)
    oralloy_amount_2 = calculate_oralloy_amount(oralloy_types[oralloy_type]['percentage'], uranium_mass_2)

    # Calculating the total amount of Oralloy
    total_oralloy_amount = oralloy_amount_1 + oralloy_amount_2

    # Displaying the results
    print("Amount of Oralloy required:")
    print(f"{oralloy_types[oralloy_type]['name']} for the first uranium sample: {oralloy_amount_1:.3f} kg")
    print(f"{oralloy_types[oralloy_type]['name']} for the second uranium sample: {oralloy_amount_2:.3f} kg")
    print(f"Total amount of Oralloy required: {total_oralloy_amount:.3f} kg")

