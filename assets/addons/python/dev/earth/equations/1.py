import math
import matplotlib.pyplot as plt

# Propriedades da Terra
raio_terrestre = 6371  # em quilômetros
densidade_media = 5515  # em kg/m³

def calcular_distribuicao_massa(raio):
    # Cálculo da distribuição de massa em relação ao raio
    volume = (4/3) * math.pi * (raio**3)
    massa = densidade_media * volume
    
    return massa

def calcular_pressao(raio):
    # Cálculo da pressão dentro do raio
    pressao = (2/3) * math.pi * densidade_media * (raio ** 2)
    
    return pressao

# Valores de raio
raios = range(1, raio_terrestre + 1)

# Listas para armazenar os resultados
distribuicao_massa = []
pressao = []

# Calcular os valores para cada raio
for raio in raios:
    distribuicao_massa.append(calcular_distribuicao_massa(raio))
    pressao.append(calcular_pressao(raio))

# Ajustar o tamanho da figura
plt.figure(figsize=(8, 6))

# Plotar o gráfico
plt.plot(raios, distribuicao_massa, label='Distribuição de Massa')
plt.plot(raios, pressao, label='Pressão')
plt.xlabel('Raio (km)')
plt.ylabel('Valor')
plt.title('Distribuição de Massa e Pressão em relação ao Raio (Propriedades da Terra)')

# Submenu com as propriedades da Terra e valores numéricos
props_terrestres = f'Raio Terrestre: {raio_terrestre} km\nDensidade Média: {densidade_media} kg/m³'
resultados_numericos = f'Valor da Massa: {distribuicao_massa[-1]:.2e} kg\nValor da Pressão: {pressao[-1]:.2e} N/m²'
submenu_texto = f'{props_terrestres}\n\n{resultados_numericos}'
plt.text(1.02, 0.98, submenu_texto, transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

plt.legend()

# Salvar o gráfico em um arquivo .png
plt.savefig('distribuicao_massa_pressao.png', dpi=300, bbox_inches='tight')
