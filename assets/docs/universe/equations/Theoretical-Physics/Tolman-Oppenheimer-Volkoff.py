import math

# Atomic masses of elements used in nuclear fission
atomic_masses = {
    "plutonium": 244,
    "uranium": 238,
    "curium": 247,
    "neptunium": 237,
    "americium": 243,
    "berkelium": 247,
    "californium": 251,
    "thorium": 232,
    "protactinium": 231,
    "actinium": 227,
    "thallium": 208,
    "rhenium": 186,
    "promethium": 145,
    "terbium": 158,
    "europium": 152,
    "holmium": 164,
    "ytterbium": 173,
    "lutetium": 175
}

def calculate_properties(r, m, element):
    G = 6.67430e-11  # Gravitational constant in m^3/(kg·s^2)
    c = 299792458  # Speed of light in vacuum in m/s

    v = (4/3) * math.pi * r**3
    ρ = m / v
    atomic_mass = atomic_masses[element]
    P = (G * (ρ + c**2 * (m / (4*math.pi*r**3)))) / (3 * (1 - (2 * G * m) / (r * c**2 * atomic_mass)))
    dP_dr = - G * (ρ + P) * (m + (4/3) * math.pi * r**3 * P) / (r * (r - (2 * G * m) / (c**2 * atomic_mass)))

    return ρ, P, dP_dr

def create_cluster():
    num_layers = int(input("Enter the number of layers in the cluster: "))

    cluster = []

    for i in range(num_layers):
        print(f"\nLayer {i+1}:")
        radius_unit = input("Choose the unit of measurement for the radius (1 for m, 2 for cm, 3 for mm): ")
        radius_option = int(radius_unit)
        radius = float(input("Enter the radius: "))

        mass_unit = input("Choose the mass unit (1 for t, 2 for kg, 3 for g, 4 for mg): ")
        mass_option = int(mass_unit)
        mass = float(input("Enter the mass: "))

        element = input("Choose the element (plutonium, uranium, curium): ")

        # Conversion of units to meters and kilograms
        if radius_option == 2:
            radius /= 100.0
        elif radius_option == 3:
            radius /= 1000.0

        if mass_option == 1:
            mass *= 1000.0
        elif mass_option == 3:
            mass /= 1000.0
        elif mass_option == 4:
            mass /= 1000000.0

        density, pressure, dP_dr = calculate_properties(radius, mass, element)
        layer = {"Radius": radius, "Mass": mass, "Density": density, "Pressure": pressure, "dP/dr": dP_dr}
        cluster.append(layer)

    return cluster

# Create the cluster
cluster = create_cluster()

# Display the properties of each layer
print("\nCluster Properties:")

for i, layer in enumerate(cluster):
    print(f"\nLayer {i+1}:")
    print("Radius: {:.2f} meters".format(layer["Radius"]))
    print("Mass: {:.2f} kilograms".format(layer["Mass"]))
    print("Density: {:.2f} kg/m^3".format(layer["Density"]))
    print("Pressure: {:.2f} N/m^2".format(layer["Pressure"]))
    print("dP/dr: {:.2f} N/(m^2/m)".format(layer["dP/dr"]))
