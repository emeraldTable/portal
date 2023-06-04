import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

def calcular_massa_estrela(luminosidade):
    # Constante de proporção para estrelas de sequência principal
    # (aproximação para estrelas de tipo espectral semelhante ao Sol)
    constante_proporcao = 1

    # Massa estimada da estrela
    massa_estrela = luminosidade / constante_proporcao

    return massa_estrela

# Luminosidade observada da estrela (exemplo fictício)
luminosidade_estrela = 2.5e26  # em watts

# Calcular a massa estimada da estrela
massa_estrela = calcular_massa_estrela(luminosidade_estrela)

# Configuração da figura
fig, ax = plt.subplots(figsize=(8, 6))

# Desenhar o planeta (círculo)
raio_planeta = 0.5
circulo = patches.Circle((0.5, 0.5), raio_planeta, edgecolor='black', facecolor='blue')
ax.add_patch(circulo)

# Submenu com os resultados numéricos
submenu_texto = f'Massa Estimada: {massa_estrela:.2e} kg'
ax.text(0.5, 0.5, submenu_texto, transform=ax.transAxes,
         fontsize=12, verticalalignment='center', horizontalalignment='center', bbox=dict(facecolor='white', alpha=0.8))

# Configurações adicionais
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Salvar a figura em um arquivo .png
plt.savefig('planeta_massa.png', dpi=300, bbox_inches='tight')

# Mostrar a figura
plt.show()
