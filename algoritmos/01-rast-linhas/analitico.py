""" equação da reta (y - mx + b):
reta(x, y)
ponto1(x1, y1)
ponto2(x2, y2)

se x1 = x2
	para y de y1 até y2
		liga_pixel(x1, y, cor);
se não 
	m = (y2 - y1) / (x2 - x1)
	b = y2 - m * x2
para x de x1 até x2
	y = m*x + b
	liga_pixel(x, y, cor)
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def analitico(x1, x2, y1, y2):

    pontos_x = []
    pontos_y = []

    if x1 == x2 and y1 == y2:
        return [x1], [y1]
    
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    if x1 == x2:      # retas verticais
        for y in range(y1, y2 + 1):
            pontos_x.append(round(x1))
            pontos_y.append(round(y))
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        for x in range(x1, x2 + 1):
            y = m * x + b              # equação da reta
            pontos_x.append(round(x))
            pontos_y.append(round(y))

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
    print("\nDefina os pontos da linha:")
    x1, y1 = ler_ponto("p1")
    x2, y2 = ler_ponto("p2")

    x_coords, y_coords = analitico(x1, x2, y1, y2)
    
    print("Coordenadas X:", x_coords)
    print("Coordenadas Y:", y_coords)

    # 4, 1, 1, 7

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
    ax.set_title('Algoritmo Analítico')
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
        plt.pause(0.02)

# legendas
    ax.plot(x1, y1, color='green', marker='o', markersize=10, zorder=5)
    ax.plot(x2, y2, color='red', marker='o', markersize=10, zorder=5)
    fig.subplots_adjust(bottom=0.16)
    fig.text(
        0.38, 0.03,
        f'P1: ({x1}, {y1})',
        ha='center',
        fontsize=11,
        color='green'
    )
    fig.text(
        0.68, 0.03,
        f'P2: ({x2}, {y2})',
        ha='center',
        fontsize=11,
        color='red'
    )
    plt.ioff()
    plt.show(block=True)

if __name__ == "__main__":
    main()