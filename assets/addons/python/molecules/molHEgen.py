import random

def gerar_smiles_molecula():
    simbolos_atomos = ['H', 'C', 'N', 'O', 'F', 'P', 'S', 'Cl']
    comprimento_molecula = random.randint(5, 15)  # Determina o comprimento do SMILES da molécula
    
    smiles = ''
    for _ in range(comprimento_molecula):
        simbolo = random.choices(simbolos_atomos, weights=[0.2, 0.3, 0.1, 0.1, 0.05, 0.05, 0.05, 0.1])[0]
        smiles += simbolo
    
    return smiles

smiles_molecula = gerar_smiles_molecula()
print("SMILES da molécula de grande energia gerada: ", smiles_molecula)
