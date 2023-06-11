import math

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
    "lutetium": 175,
    "einsteinium": 252,
    "fermium": 257,
    "mendelevium": 258,
    "nobelium": 259,
    "lawrencium": 266,
    "rutherfordium": 267,
    "DeFi": 314
}

def calculate_sphere_weight(radius, thickness, density):
    # Calculate the internal and external volumes
    internal_volume = (4/3) * math.pi * radius**3
    external_radius = radius + thickness
    external_volume = (4/3) * math.pi * external_radius**3

    # Calculate the volume of the shell
    shell_volume = external_volume - internal_volume

    # Calculate the total weight
    total_weight = shell_volume * density

    return total_weight

def calculate_cluster_weight(cluster):
    total_weight = cluster["Total Weight"]
    radius = cluster["Radius"]
    thickness = cluster["Thickness"]
    density = cluster["Density"]
    element = cluster["Element"]
    atomic_mass = atomic_masses[element]
    element_weight = (4/3) * math.pi * (radius + thickness)**3 * density * atomic_mass

    total_cluster_weight = total_weight + element_weight

    return total_cluster_weight

def create_cluster():
    num_clusters = int(input("Enter the number of clusters: "))
    clusters = []
    for i in range(num_clusters):
        print(f"\nCluster {i+1}:")
        radius = float(input("Enter the radius of the sphere (in meters): "))
        thickness = float(input("Enter the thickness of the sphere (in meters): "))
        density = float(input("Enter the density of the alloy (in kg/m^3): "))
        element = input("Enter the element (plutonium, DeFi): ")

        total_weight = calculate_sphere_weight(radius, thickness, density)
        total_cluster_weight = calculate_cluster_weight({
            "Total Weight": total_weight,
            "Radius": radius,
            "Thickness": thickness,
            "Density": density,
            "Element": element
        })

        cluster = {
            "Radius": radius,
            "Thickness": thickness,
            "Density": density,
            "Total Weight": total_weight,
            "Element": element,
            "Total Cluster Weight": total_cluster_weight
        }
        clusters.append(cluster)

    return clusters

# Create the clusters
clusters = create_cluster()

# Display the results for each cluster
print("\nCluster Properties:")
for i, cluster in enumerate(clusters):
    print(f"\nCluster {i+1}:")
    print("Radius: {:.2f} meters".format(cluster["Radius"]))
    print("Thickness: {:.2f} meters".format(cluster["Thickness"]))
    print("Density: {:.2f} kg/m^3".format(cluster["Density"]))
    print("Total Weight: {:.2f} kg".format(cluster["Total Weight"]))
    print("Element: {}".format(cluster["Element"]))
    print("Total Cluster Weight: {:.2f} kg".format(cluster["Total Cluster Weight"]))
