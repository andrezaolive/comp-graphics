"""
reta(x, y)
ponto1(x1, y1)
ponto2(x2, y2)
dy = y2 – y1; 
dx = x2 – x1; 
y = y1;
p = 2dy – dx;
para (x = x1 -> x2) {
WritePixel(x, y);
se (p ≥ 0) {
y = y + 1;
p = p + 2(dy – dx);
se não {p = p + 2dy;}
}
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def bresenham(x1, x2, y1, y2):

    pontos_x = []
    pontos_y = []

    if x1 == x2 and y1 == y2:
        return [x1], [y1]

    passo_x = 1 if x1 < x2 else -1
    passo_y = 1 if y1 < y2 else -1
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x = x1
    y = y1 
    p = 2 * dy - dx # parâmetro de decisão inicial

    if dx > dy:
        p = 2 * dy - dx
        # o laço roda 'dx' vezes, que é a maior distância
        for _ in range(dx + 1):
            pontos_x.append(x)
            pontos_y.append(y)
            
            if p >= 0:
                y += passo_y
                p += 2 * (dy - dx) # parâmetro de decisão incremental
            else:
                p += 2 * dy
            x += passo_x 
    else:
        p = 2 * dx - dy
        # o laço roda 'dy' vezes, que é a maior distância
        for _ in range(dy + 1):
            pontos_x.append(x)
            pontos_y.append(y)
            
            if p >= 0:
                x += passo_x
                p += 2 * (dx - dy) # parâmetro de decisão incremental
            else:
                p += 2 * dx
            y += passo_y 

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

    x_coords, y_coords = bresenham(x1, x2, y1, y2)
    
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