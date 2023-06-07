import random

def gerador_sequencia():
    amino_acidos = {
        "Met": "AUG",
        "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
        "Thr": ["ACU", "ACC", "ACA", "ACG"],
        "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
        "Glu": ["GAA", "GAG"],
        "Lys": ["AAA", "AAG"],
        "Gln": ["CAA", "CAG"],
        "Gly": ["GGU", "GGC", "GGA", "GGG"],
        "Ala": ["GCU", "GCC", "GCA", "GCG"],
        "Val": ["GUU", "GUC", "GUA", "GUG"],
        "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
        "Cys": ["UGU", "UGC"],
        "Asp": ["GAU", "GAC"],
        "Phe": ["UUU", "UUC"],
        "Ile": ["AUU", "AUC", "AUA"],
        "Asn": ["AAU", "AAC"]
    }

    sequencia = ""
    comprimento = 250

    for _ in range(comprimento):
        amino_acido = random.choice(list(amino_acidos.keys()))
        codons = amino_acidos[amino_acido]
        codon = random.choice(codons)
        sequencia += amino_acido + "-"

    sequencia = sequencia[:-1]  # Remove o último hífen

    return sequencia

sequencia_gerada = gerador_sequencia()
print(sequencia_gerada)
