"""
fcircle(x,y) = x2 + y2 - R2

x = 0
y = r
p = 1 - r # parâmetro de decisão
while x <= y
	pixel(x, y, cor)
	if p >= 0:
		y = y - 1
		p = p + 2x - 2y + 5
		x = x + 1
	else:
		p = p + 2x + 3
		x = x + 1
"""
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def bresenham_cir(xc, yc, r):

    pontos_x = []
    pontos_y = []

    x = 0
    y = r
    p = 1 - r

    while x <= y:
        pontos_x.append(x + xc)
        pontos_y.append(y + yc)
        pontos_x.append(y + xc)
        pontos_y.append(x + yc)
        pontos_x.append(x + xc)
        pontos_y.append(-y + yc)
        pontos_x.append(-x + xc)
        pontos_y.append(y + yc)

        pontos_x.append(-y + xc)
        pontos_y.append(x + yc)
        pontos_x.append(y + xc)
        pontos_y.append(-x + yc)
        pontos_x.append(-x + xc)
        pontos_y.append(-y + yc)
        pontos_x.append(-y + xc)
        pontos_y.append(-x + yc)

        if p >= 0:  # o ponto médio teórico está fora (ou sobre) a curva exata
            y = y - 1
            p = p + 2 * x - 2 * y + 5
            x = x + 1
        else:
            p = p + 2 * x + 3
            x = x + 1

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

    x_coords, y_coords = bresenham_cir(xc, yc, r)
    
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
    ax.set_title('Algoritmo Bresenham')
    ax.set_xlabel('Coordenadas X')
    ax.set_ylabel('Coordenadas Y')

    plt.ion() # modo interativo para permitir atualização dinâmica do gráfico
    # Mostra cada pixel somente depois que a janela já está configurada
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
        plt.pause(0.01)
    
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