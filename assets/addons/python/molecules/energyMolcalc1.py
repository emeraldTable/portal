tabela_periodica = {
    'H': {'energia': 4.5},
    'He': {'energia': 24.6},
    'Li': {'energia': 5.4},
    'Be': {'energia': 9.3},
    'B': {'energia': 8.3},
    'C': {'energia': 7.5},
    'N': {'energia': 10.0},
    'O': {'energia': 12.0},
    'F': {'energia': 15.0},
    'Ne': {'energia': 21.6},
    'Na': {'energia': 5.1},
    'Mg': {'energia': 7.6},
    'Al': {'energia': 5.9},
    'Si': {'energia': 8.2},
    'P': {'energia': 10.5},
    'S': {'energia': 10.4},
    'Cl': {'energia': 12.0},
    'Ar': {'energia': 15.8},
    'K': {'energia': 4.3},
    'Ca': {'energia': 6.1},
    'Sc': {'energia': 6.6},
    'Ti': {'energia': 6.8},
    'V':{'energia' :6.7 },
    'Cr':{'energia' :6.8 },
    'Mn':{'energia' :7.4 },
    'Fe':{'energia' :7.9 },
    'Co':{'energia' :7.7 },
    'Ni':{'energia' :7.6 },
    'Cu':{'energia' :7.7 },
    'Zn':{'energia' :9.4 },
    'Ga':{'energia' :5.9 },
    'Ge':{'energia' :7.9 },
    'As':{'energia' :9.8 },
    'Se':{'energia' :9.8 },
    'Br':{'energia' :11.8 },
    'Kr':{'energia' :14.0 },
    'Rb':{'energia' :4.2 },
    'Sr':{'energia' :5.0 },
    'Y':{'energia' :6.2 },
    'Zr':{'energia' :6.6 },
    'Nb':{'energia' :6.8 },
    'Mo':{'energia' :7.1 },
    'Tc':{'energia' :7.3 },
    'Ru':{'energia' :7.2 },
    'Rh':{'energia' :7.5 },
    'Pd':{'energia' :8.3 },
    'Ag':{'energia' :7.6 },
    'Cd':{'energia' :8.9 },
    'In':{'energia' :5.8 },
    'Sn':{'energia' :7.3 },
    'Sb':{'energia' :8.6 },
    'Te':{'energia' :9.0 },
    'I':{'energia' :10.5 },
    "Xe": {"energy":12}
}


def calcular_energia_molecula(molecula):
    energia_total = 0
    for elemento, quantidade in molecula.items():
        energia_atomo = tabela_periodica[elemento]['energia']
        energia_total += energia_atomo * quantidade
    return energia_total

def converter_smiles_para_molecula(smiles):
    molecula = {}
    i = 0
    while i < len(smiles):
        elemento = smiles[i]
        quantidade = 1
        i += 1
        if i < len(smiles) and smiles[i].isdigit():
            quantidade = int(smiles[i])
            i += 1
        if elemento in molecula:
            molecula[elemento] += quantidade
        else:
            molecula[elemento] = quantidade
    return molecula

# Obter o SMILES da molécula do usuário
smiles = input("Insira o SMILES da molécula: ")

# Converter o SMILES para uma molécula
molecula = converter_smiles_para_molecula(smiles)

# Calcular a energia da molécula
energia_molecula = calcular_energia_molecula(molecula)

# Exibir o resultado
print(f"A energia total da molécula é: {energia_molecula} eV")
