import math

megatons_produced = 15111
mass_hydrogen = 702000

# Fission reaction equation
fission_equation = "Fission reaction: E = mc^2"
fission_energy = mass_hydrogen * math.pow(3e8, 2)  # E = mc^2

# Compression and implosion equation
compression_equation = "Compression and implosion: V = πr^2h"
radius = math.pow((3 * mass_hydrogen) / (4 * math.pi), 1 / 3)
height = (4 * mass_hydrogen) / (3 * math.pi * math.pow(radius, 2))
compression_volume = math.pi * math.pow(radius, 2) * height  # V = πr^2h

# Compression mechanism equation
compression_mechanism_equation = "Compression mechanism: F = ma"
acceleration = (3e8 ** 2 * mass_hydrogen) / (radius * height)
compression_force = mass_hydrogen * acceleration  # F = ma

# Implosion initiation equation
implosion_initiation_equation = "Implosion initiation: P = F/A"
area = math.pi * math.pow(radius, 2)
implosion_pressure = compression_force / area  # P = F/A

# Nuclear fusion equation
fusion_equation = "Nuclear fusion: E = mc^2"
fusion_energy = mass_hydrogen * math.pow(3e8, 2)  # E = mc^2

# Extreme compression equation
extreme_compression_equation = "Extreme compression: P = F/A"
extreme_compression_pressure = implosion_pressure  # P = F/A

# Fusion reaction initiation equation
fusion_reaction_initiation_equation = "Fusion reaction initiation: Q = mcΔT"
temperature_change = megatons_produced / (mass_hydrogen * 4.184 * 1e9)
fusion_reaction_initiation_energy = mass_hydrogen * 3e8 * temperature_change  # Q = mcΔT

# Helium-4 production equation
helium_4_production_equation = "Helium-4 production: n = N/λt"
decay_constant = 4.95e-22
helium_4_production = megatons_produced / (decay_constant * 1e6 * mass_hydrogen)

# Release of energy equation
release_of_energy_equation = "Release of energy: KE = 0.5mv^2"
velocity = math.sqrt((2 * megatons_produced * 4.184 * 1e9) / mass_hydrogen)
kinetic_energy = 0.5 * mass_hydrogen * math.pow(velocity, 2)  # KE = 0.5mv^2


# Printing the explanations
print(fission_equation)
print("Energy produced in the fission reaction: {} joules\n".format(fission_energy))

print(compression_equation)
print("Volume of compression and implosion: {} cubic meters\n".format(compression_volume))

print(compression_mechanism_equation)
print("Force applied by the compression mechanism: {} newtons\n".format(compression_force))

print(implosion_initiation_equation)
print("Pressure exerted during implosion initiation: {} pascals\n".format(implosion_pressure))

print(fusion_equation)
print("Energy released in nuclear fusion: {} joules\n".format(fusion_energy))

print(extreme_compression_equation)
print("Pressure during extreme compression: {} pascals\n".format(extreme_compression_pressure))

print(fusion_reaction_initiation_equation)
print("Energy required for fusion reaction initiation: {} joules\n".format(fusion_reaction_initiation_energy))

print(helium_4_production_equation)
print("Number of helium-4 produced: {} particles\n".format(helium_4_production))

print(release_of_energy_equation)
print("Kinetic energy released: {} joules\n".format(kinetic_energy))
