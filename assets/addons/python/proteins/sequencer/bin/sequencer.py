import random

def gerador_sequencia():
    amino_acidos = ["Met", "Arg", "Thr", "Ser", "Glu", "Lys", "Gln", "Gly", "Ala", "Val", "Leu", "Cys", "Asp", "Phe", "Ile", "Asn"]

    sequencia = ""
    comprimento = random.randint(100, 200)  # Defina o comprimento desejado da sequência

    for _ in range(comprimento):
        amino_acido = random.choice(amino_acidos)
        sequencia += amino_acido + "-"

    sequencia = sequencia[:-1]  # Remove o último hífen

    return sequencia

sequencia_gerada = gerador_sequencia()
print(sequencia_gerada)
