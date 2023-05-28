import random

# Prompting user for inputs
print("Ivy Mike Bomb Recreation Steps")
print("-------------------------------")
name = input("Your name: ")
year = input("Current year: ")
designer = input("Bomb designer: ")

initial_steps = [
    "Design and construction: Designed and constructed by {}.".format(designer),
    "Fission reaction: Initiate nuclear fission using enriched plutonium or uranium core.",
    "Compression and implosion: Compress and implode deuterium capsule around lithium-6 core.",
    "Nuclear fusion: Extreme compression and implosion cause deuterium fusion, producing helium-4 and releasing massive energy.",
    "Termonuclear effect: Fusion releases 10.4 megatons of TNT energy."
]

additional_steps = [
    "Radiation effects: Widespread ionizing radiation and radioactive fallout.",
    "Blast wave: Generates destructive shockwave.",
    "Fireball formation: Massive fireball from intense heat.",
    "Mushroom cloud formation: Distinctive mushroom-shaped cloud from rapid ascent and cooling of vaporized material.",
    "Environmental impact: Long-lasting contamination and environmental consequences.",
    "Humanitarian considerations: Raises ethical and humanitarian concerns."
]

# Randomly selecting a method for nuclear fission reaction
selected_method = random.choice([
    "Gun-type design: Sub-critical mass fired into larger, supercritical mass.",
    "Implosion design: Sub-critical mass surrounded by explosives, compressing the core.",
    "Spherical implosion design: Hollow core compressed symmetrically."
])

# Steps for compression and implosion
compression_steps = [
    "Deuterium capsule: Prepare deuterium capsule.",
    "Lithium-6 core: Place lithium-6 core inside the capsule.",
    "Compression mechanism: Develop compression mechanism.",
    "Implosion initiation: Initiate rapid implosion of the capsule."
]

# Steps for nuclear fusion
fusion_steps = [
    "Extreme compression: Implosion mechanism creates extreme compression.",
    "Fusion reaction initiation: Trigger nuclear fusion between deuterium and lithium-6 atoms.",
    "Helium-4 production: Production of helium-4 nuclei.",
    "Release of energy: Massive release of energy in the form of photons and kinetic energy."
]

# Writing steps to file
filename = "ivy_mike_steps.txt"
with open(filename, "w") as file:
    file.write("Ivy Mike Bomb Recreation Steps\n")
    file.write("-----------------------------\n")
    file.write("Name: {}\n".format(name))
    file.write("Year: {}\n".format(year))
    file.write("Designer: {}\n\n".format(designer))
    file.write("Initial Steps:\n")
    for step in initial_steps:
        if step.startswith("Fission"):
            file.write("- {}: {}\n".format(step, selected_method))
        elif step.startswith("Compression"):
            file.write("- {}:\n".format(step))
            for compression_step in compression_steps:
                file.write("  - {}\n".format(compression_step))
        elif step.startswith("Nuclear"):
            file.write("- {}:\n".format(step))
            for fusion_step in fusion_steps:
                file.write("  - {}\n".format(fusion_step))
        else:
            file.write("- {}\n".format(step))
    file.write("\nAdditional Steps:\n")
    for step in additional_steps:
        file.write("- {}\n".format(step))

print("\nSteps have been saved to {}.".format(filename))
