"""
x = xc + r . cos (t)
y = yc + r . sen (t)

x = xc + raio
y = yc

para t de 1 a 360
	pixel (x, y, cor)
	x = xc + r . cos((pi . t) / 180)
	y = yc + r . sen((pi . t) / 180)
"""
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def parametrico(xc, yc, r):

    pontos_x = []
    pontos_y = []

    x = xc + r
    y = yc    # posiciona na extrema direita

    for t in range(1, 361):
        pontos_x.append(round(x))
        pontos_y.append(round(y))
        # equações paramétricas que calculam o próximo ponto
        x = xc + r * math.cos((math.pi * t) / 180)
        y = yc + r * math.sin((math.pi * t) / 180)

    return pontos_x, pontos_y

def ler_ponto(nome):
    while True:
        try:
            print(f"Digite o {nome} (ex: 1,1): ", end="", flush=True)
            ponto = input().strip()
            x, y = ponto.split(",")
            return int(x.strip()), int(y.strip())
        except ValueError:
            print("Entrada invalida. Use o formato x,y, por exemplo: 1,1")


def main():
    print("\nDefina os pontos do centro da circunferência:")
    xc, yc = ler_ponto("centro")
    r = int(input("Digite o raio da circunferência: "))

    x_coords, y_coords = parametrico(xc, yc, r)
    
    print("Coordenadas X:", x_coords)
    print("Coordenadas Y:", y_coords)

    fig, ax = plt.subplots(figsize=(7, 7))
    
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    # pixels
    ax.set_xticks(range(min_x - 3, max_x + 3))
    ax.set_yticks(range(min_y - 3, max_y + 3))
    # grade
    ax.set_xticks([value - 0.5 for value in range(min_x - 3, max_x + 3)], minor=True)
    ax.set_yticks([value - 0.5 for value in range(min_y - 3, max_y + 3)], minor=True)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, which='minor', color='black', linewidth=0.8)
    ax.set_axisbelow(False)
    ax.set_title('Algoritmo Paramétrico')
    ax.set_xlabel('Coordenadas X')
    ax.set_ylabel('Coordenadas Y')

    plt.ion() # modo interativo para permitir atualização dinâmica do gráfico
    # mostra cada pixel somente depois que a janela está configurada
    plt.show(block=False)
    for x, y in zip(x_coords, y_coords):
        ax.add_patch(
            Rectangle(
                (x - 0.5, y - 0.5),
                1,
                1,
                facecolor="black",
                edgecolor="black",
                zorder=3,
            )
        )
        fig.canvas.draw_idle()
        fig.canvas.flush_events()
        plt.pause(0.001)
    
    # legendas
    ax.plot(xc, yc, color='blue', marker='s', markersize=10, zorder=5)
    fig.subplots_adjust(bottom=0.16)
    fig.text(
        0.38, 0.03,
        f'Centro: ({xc}, {yc})',
        ha='center',
        fontsize=11,
        color='blue'
    )
    fig.text(
        0.68, 0.03,
        f'Raio: {r}',
        ha='center',
        fontsize=11,
        color='red'
    )
    plt.ioff()
    plt.show(block=True)

if __name__ == "__main__":
    main()