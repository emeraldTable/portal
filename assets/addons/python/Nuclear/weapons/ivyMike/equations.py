import sympy
# User input for megatons produced and mass of hydrogen used to produce the bomb
megatons_produced = float(input("Enter the megatons produced by the bomb: "))
mass_hydrogen = float(input("Enter the mass of hydrogen used to produce the bomb (in kg): "))

# Fission equation
m_fission = sympy.symbols('m_fission')
c = sympy.symbols('c')
fission_equation = sympy.Eq(m_fission, megatons_produced * c**2)

# Compression and implosion equations
V_deuterium = sympy.symbols('V_deuterium')
r = sympy.symbols('r')
deuterium_capsule_equation = sympy.Eq(V_deuterium, mass_hydrogen * r**3)
V_lithium6 = sympy.symbols('V_lithium6')
lithium_6_core_equation = sympy.Eq(V_lithium6, mass_hydrogen * r**3)
F_compression = sympy.symbols('F_compression')
A = sympy.symbols('A')
compression_mechanism_equation = sympy.Eq(F_compression, mass_hydrogen * A)
F_implosion = sympy.symbols('F_implosion')
t = sympy.symbols('t')
implosion_initiation_equation = sympy.Eq(F_implosion, mass_hydrogen * t)

# Nuclear fusion equations
P_extreme = sympy.symbols('P_extreme')
extreme_compression_equation = sympy.Eq(P_extreme, megatons_produced * A)
E_fusion = sympy.symbols('E_fusion')
fusion_reaction_initiation_equation = sympy.Eq(E_fusion, megatons_produced * t)
N_helium4 = sympy.symbols('N_helium4')
helium_4_production_equation = sympy.Eq(N_helium4, megatons_produced * m_fission)
E_energy = sympy.symbols('E_energy')
release_of_energy_equation = sympy.Eq(E_energy, megatons_produced * c**2)

# Termonuclear effect equation
E_termonuclear = sympy.symbols('E_termonuclear')
termonuclear_effect_equation = sympy.Eq(E_termonuclear, megatons_produced)

# Additional equations
X_radiation = sympy.symbols('X_radiation')
radiation_effects_equation = sympy.Eq(X_radiation, megatons_produced)
P_blast = sympy.symbols('P_blast')
blast_wave_equation = sympy.Eq(P_blast, megatons_produced)
T_fireball = sympy.symbols('T_fireball')
fireball_formation_equation = sympy.Eq(T_fireball, megatons_produced)
H_mushroom = sympy.symbols('H_mushroom')
mushroom_cloud_formation_equation = sympy.Eq(H_mushroom, megatons_produced)
C_environmental = sympy.symbols('C_environmental')
environmental_impact_equation = sympy.Eq(C_environmental, megatons_produced)
H_humanitarian = sympy.symbols('H_humanitarian')
humanitarian_considerations_equation = sympy.Eq(H_humanitarian, megatons_produced)

# Solving the equations
solutions = sympy.solve([
    fission_equation,
    deuterium_capsule_equation,
    lithium_6_core_equation,
    compression_mechanism_equation,
    implosion_initiation_equation,
    extreme_compression_equation,
    fusion_reaction_initiation_equation,
    helium_4_production_equation,
    release_of_energy_equation,
    termonuclear_effect_equation,
    radiation_effects_equation,
    blast_wave_equation,
    fireball_formation_equation,
    mushroom_cloud_formation_equation,
    environmental_impact_equation,
    humanitarian_considerations_equation
])

# Writing the solutions to file
filename = "ivy_mike_equations.txt"
with open(filename, "w") as file:
    file.write("Ivy Mike Bomb Equations\n")
    file.write("-----------------------\n")
    for equation in solutions:
        file.write("{}\n".format(equation))

print("Equations have been saved to {}.".format(filename))
