import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotar_massa_lua(massa_terra, massa_lua, distancia_media, periodo_orbital):
    # Criação da figura e do objeto Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Escala das esferas
    escala_terra = (massa_terra / massa_terra) ** (1/3)  # Escala da Terra (1)
    escala_lua = (massa_lua / massa_terra) ** (1/3)  # Escala da Lua em relação à Terra


    # Plotar a esfera da Terra
    ax.scatter(distancia_media, 0, 0, color='blue', s=escala_terra**2 * 1000, label='Terra')

    # Plotar a esfera da Lua
    ax.scatter(0, 0, 0, color='gray', s=escala_lua**2 * 1000, label='Lua')
    # Configurações adicionais
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')

    # Adicionar a escala de distância e o período orbital na caixa de texto
    texto = f'Distância Média: {distancia_media} km\nPeríodo Orbital: {periodo_orbital} dias\nEarth Mass: {massa_terra} kg\nMoon Mass {massa_lua} kg'
    ax.text2D(0.02, 0.98, texto, transform=ax.transAxes, ha='left', va='top', bbox={'facecolor': 'white', 'alpha': 0.8})

    # Exibir a legenda
    ax.legend()

    # Salvar a figura como imagem .png
    plt.savefig('massa_lua.png', dpi=300)

    # Mostrar a figura (opcional)
    # plt.show()

# Valores de exemplo para a massa da Terra, da Lua, distância média e período orbital
massa_terra = 5.972e24  # kg
massa_lua = 7.35e22  # kg
distancia_media = 384400  # km
periodo_orbital = 27.322  # dias

# Chamada da função para plotar a massa da Terra e da Lua em uma imagem .png
plotar_massa_lua(massa_terra, massa_lua, distancia_media, periodo_orbital)
