tabela_periodica = {
    'H': {'energia': 4.5},
    'C': {'energia': 7.5},
    'N': {'energia': 10.0},
    'O': {'energia': 12.0},
    'F': {'energia': 15.0},
    'P': {'energia': 18.0},
    'S': {'energia': 20.0},
    'Cl': {'energia': 22.0}
}

def calcular_energia_molecula(molecula):
    energia_total = 0
    for elemento, quantidade in molecula.items():
        energia_atomo = tabela_periodica[elemento]['energia']
        energia_total += energia_atomo * quantidade
    return energia_total

# Gerar a molécula
import random

def gerar_molecula():
    molecula = {}
    simbolos_atomos = ['H', 'C', 'N', 'O', 'F', 'P', 'S', 'Cl']
    comprimento_molecula = random.randint(5, 15)  # Determina o comprimento do SMILES da molécula
    
    for _ in range(comprimento_molecula):
        simbolo = random.choices(simbolos_atomos, weights=[0.2, 0.3, 0.1, 0.1, 0.05, 0.05, 0.05, 0.1])[0]
        if simbolo in molecula:
            molecula[simbolo] += 1
        else:
            molecula[simbolo] = 1
    
    return molecula

# Exemplo de uso:
molecula_gerada = gerar_molecula()
energia_molecula = calcular_energia_molecula(molecula_gerada)
print(f"A energia total da molécula gerada é: {energia_molecula} eV")
print(f"Molécula gerada: {molecula_gerada}")
