import random

# Generate a random molecule name
molecule_name = "CHEMDOOD" + str(random.randint(0, 99999999999)).zfill(11)

# Generate random atom positions and types
atoms = []
for _ in range(14):
    x = round(random.uniform(-2, 2), 4)
    y = round(random.uniform(-2, 2), 4)
    z = round(random.uniform(-2, 2), 4)
    atom_type = random.choice(["O", "C", "N"])
    atoms.append((x, y, z, atom_type))

# Generate random bond connections
bonds = []
for i in range(1, 15):
    num_bonds = random.randint(0, 3)
    connected_atoms = random.sample(range(1, 15), num_bonds)
    for atom in connected_atoms:
        bond_type = random.choice([1, 2])
        if (atom, i, bond_type) not in bonds and (i, atom, bond_type) not in bonds:
            bonds.append((i, atom, bond_type))

# Generate the final molecule representation
molecule = f"Molecule Name\n  {molecule_name} 0   0.00000     0.00000     0\n[Insert Comment Here]\n 14 15  0  0  0  0  0  0  0  0  1 V2000\n"
for i, atom in enumerate(atoms, start=1):
    x, y, z, atom_type = atom
    molecule += f"   {x:8.4f}    {y:8.4f}    {z:8.4f}   {atom_type} 0  0  0  1  0  0  0  0  0  0  0  0\n"
for bond in bonds:
    atom1, atom2, bond_type = bond
    molecule += f" {atom1:3d} {atom2:3d} {bond_type}  0  0  0  0\n"
molecule += "M  END\n> <DATE>\n07-08-2009\n"

# Print the generated molecule
print(molecule)
