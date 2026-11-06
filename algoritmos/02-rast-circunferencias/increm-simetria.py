"""
x = r; 
y = 0; 
θ = 1/r
while y <= x
	pixel (x + xc, y + yc, cor)
    pixel (y + xc, x + yc, cor)
    pixel (x + xc, -y + yc, cor)
    pixel (-x + xc, y + yc, cor)
xt = x
x = x ⋅ cos (θ) – y . sen(θ)
y = y ⋅ cos(θ) + xt . sen(θ)
"""
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def increm_simetria(xc, yc, r):

    pontos_x = []
    pontos_y = []

    x = r
    y = 0
    t = 1 / r   # um ângulo constante para incrementar

    cost = math.cos(t)
    sent = math.sin(t)

    while y <= x:
        pontos_x.append(round(x + xc))
        pontos_y.append(round(y + yc))

        pontos_x.append(round(y + xc))
        pontos_y.append(round(x + yc))

        pontos_x.append(round(x + xc))
        pontos_y.append(round(-y + yc))

        pontos_x.append(round(-x + xc))
        pontos_y.append(round(y + yc))

        pontos_x.append(round(-y + xc))
        pontos_y.append(round(x + yc))

        pontos_x.append(round(y + xc))
        pontos_y.append(round(-x + yc))

        pontos_x.append(round(-x + xc))
        pontos_y.append(round(-y + yc))

        pontos_x.append(round(-y + xc))
        pontos_y.append(round(-x + yc))

        xt = x
        x = x * cost - y * sent
        y = y * cost + xt * sent
    
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

    x_coords, y_coords = increm_simetria(xc, yc, r)

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
    ax.set_title('Algoritmo Incremental com Simetria')
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