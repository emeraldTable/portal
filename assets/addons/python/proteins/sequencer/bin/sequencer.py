import random

def generate_amino_acid_sequence(category, length):
    amino_acids = {
        'polar': ['Ser', 'Thr', 'Asn', 'Gln'],
        'nonpolar': ['Ala', 'Gly', 'Val', 'Leu'],
        'charged': ['Arg', 'Lys', 'Asp', 'Glu'],
        'aromatic': ['Phe', 'Tyr', 'Trp', 'His']
    }

    if category not in amino_acids:
        raise ValueError(f"Invalid category: {category}")

    sequence = ""
    for _ in range(length):
        sequence += random.choice(amino_acids[category])

    return sequence

# Example usage
sequence = generate_amino_acid_sequence('polar', 10)
formatted_sequence = " ".join([sequence[i:i+3] for i in range(0, len(sequence), 3)])

print(formatted_sequence)
