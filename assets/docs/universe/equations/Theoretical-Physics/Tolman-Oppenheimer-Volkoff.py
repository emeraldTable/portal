import math

def calculate_properties(radius, mass):
    G = 6.67430e-11  # Constante gravitacional em m^3/(kg·s^2)
    c = 299792458  # Velocidade da luz no vácuo em m/s

    volume = (4/3) * math.pi * radius**3
    density = mass / volume
    pressure = (G * (density + c**2 * (mass / (4*math.pi*radius**3)))) / (3 * (1 - (2 * G * mass) / (radius * c**2)))
    dP_dr = - G * (density + pressure) * (mass + (4/3) * math.pi * radius**3 * pressure) / (radius * (radius - (2 * G * mass) / c**2))

    return density, pressure, dP_dr

def create_cluster():
    num_layers = int(input("Digite o número de camadas do cluster: "))

    cluster = []

    for i in range(num_layers):
        print(f"\nCamada {i+1}:")
        radius_unit = input("Escolha a unidade de medida para o raio (m, cm, mm): ")
        radius = float(input("Informe o raio: "))

        mass_unit = input("Escolha a unidade de massa (t, kg, g, mg): ")
        mass = float(input("Informe a massa: "))

        # Conversão das unidades para metros e quilogramas
        if radius_unit == "cm":
            radius /= 100.0
        elif radius_unit == "mm":
            radius /= 1000.0

        if mass_unit == "t":
            mass *= 1000.0
        elif mass_unit == "g":
            mass /= 1000.0
        elif mass_unit == "mg":
            mass /= 1000000.0

        density, pressure, dP_dr = calculate_properties(radius, mass)
        layer = {"Raio": radius, "Massa": mass, "Densidade": density, "Pressão": pressure, "dP/dr": dP_dr}
        cluster.append(layer)

    return cluster

# Criação do cluster
cluster = create_cluster()

# Exibição das propriedades de cada camada
print("\nPropriedades do Cluster:")

for i, layer in enumerate(cluster):
    print(f"\nCamada {i+1}:")
    print("Raio: {:.2f} metros".format(layer["Raio"]))
    print("Massa: {:.2f} quilogramas".format(layer["Massa"]))
    print("Densidade: {:.2f} kg/m^3".format(layer["Densidade"]))
    print("Pressão: {:.2f} N/m^2".format(layer["Pressão"]))
    print("dP/dr: {:.2f} N/(m^2/m)".format(layer["dP/dr"]))
