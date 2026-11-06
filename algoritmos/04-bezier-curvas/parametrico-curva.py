"""
bezier_quad(P0, P1, P2, t):
    return (1 - t) ** 2 * P0 + 2 * (1 - t) * t * P1 + t ** 2 * P2

bezier_cubica(P0, P1, P2, P3, t):
    return (1 - t) ** 3 * P0 + 3 * (1 - t) ** 2 * t * P1 + 3 * (1 - t) * t ** 2 * P2 + t ** 3 * P3

"""
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def bezier_quadratic(P0, P1, P2, t):

    # curva de Bézier quadrática
    return math.pow(1 - t, 2) * P0 + 2 * (1 - t) * t * P1 + math.pow(t, 2) * P2

def bezier_cubic(P0, P1, P2, P3, t):
    
    # curva de Bézier cúbica
    return math.pow(1 - t, 3) * P0 + 3 * math.pow(1 - t, 2) * t * P1 + 3 * (1 - t) * math.pow(t, 2) * P2 + math.pow(t, 3) * P3


def ler_ponto(nome):
    while True:
        try:
            print(f"Digite o {nome} (ex: 1,1): ", end="", flush=True)
            ponto = input().strip()
            x, y = ponto.split(",")
            return np.array([int(x.strip()), int(y.strip())])

        except ValueError:
            print("Entrada invalida. Use o formato x,y, por exemplo: 1,1")


def main():
    print("Algoritmo paramétrico para curvas de Bézier")
    print("\nEscolha o tipo de curva que deseja desenhar:")
    print("\n1 Curva com 3 pontos (Quadrática); \n2 Curva com 4 pontos (Cúbica); \n3 Sair")
    opcao = int(input("\nEscolha uma opção (1-3): "))
    if opcao == 1:
        funcao_curva = bezier_quadratic
        pontos_controle = [
            ler_ponto("P0"),
            ler_ponto("P1"),
            ler_ponto("P2"),
        ]
    elif opcao == 2:
        funcao_curva = bezier_cubic
        pontos_controle = [
            ler_ponto("P0"),
            ler_ponto("P1"),
            ler_ponto("P2"),
            ler_ponto("P3"),
        ]
    elif opcao == 3:
        return
    else:
        print("Opção inválida.")
        return

    t_valores = np.linspace(0, 1, 100) # fatias de t
    pontos_bezier = np.array([
        funcao_curva(*pontos_controle, t)
        for t in t_valores
    ])

    x_coords = np.rint(pontos_bezier[:, 0]).astype(int)  # discretiza e gera recursao
    y_coords = np.rint(pontos_bezier[:, 1]).astype(int)
    print("Coordenadas X:", x_coords)
    print("Coordenadas Y:", y_coords)


    fig, ax = plt.subplots(figsize=(7, 7))

    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    limite_x_min, limite_x_max = min_x - 5, max_x + 5
    limite_y_min, limite_y_max = min_y - 5, max_y + 5
    # pixels
    ax.set_xticks(range(limite_x_min, limite_x_max + 1))
    ax.set_yticks(range(limite_y_min, limite_y_max + 1))
    # grade
    ax.set_xticks([value - 0.5 for value in range(limite_x_min, limite_x_max + 2)], minor=True)
    ax.set_yticks([value - 0.5 for value in range(limite_y_min, limite_y_max + 2)], minor=True)
    ax.set_xlim(limite_x_min - 0.5, limite_x_max + 0.5)
    ax.set_ylim(limite_y_min - 0.5, limite_y_max + 0.5)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, which='minor', color='black', linewidth=0.8)
    ax.set_axisbelow(False)
    ax.set_title('Algoritmo Paramétrico para Curvas de Bézier')
    ax.set_xlabel('Coordenadas X')
    ax.set_ylabel('Coordenadas Y')
    fig.subplots_adjust(bottom=0.16)

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

    # legendas
    start_point = pontos_controle[0]
    end_point = pontos_controle[-1]
    ax.plot(start_point[0], start_point[1], color='green', marker='o', markersize=10, zorder=5)
    ax.plot(end_point[0], end_point[1], color='green', marker='o', markersize=10, zorder=5)
    ax.plot(pontos_controle[-2][0], pontos_controle[-2][1], color='blue', marker='o', markersize=10, zorder=5)
    if funcao_curva == bezier_cubic:
        ax.plot(pontos_controle[-3][0], pontos_controle[-3][1], color='blue', marker='o', markersize=10, zorder=5)
        fig.text(
                0.58, 0.03,
                f'P{len(pontos_controle) - 3}: ({pontos_controle[-3][0]}, {pontos_controle[-3][1]})',
                ha='center',
                fontsize=11,
                color='blue'
            )
    fig.text(
        0.33, 0.03,
        f'P0: ({start_point[0]}, {start_point[1]})',
        ha='center',
        fontsize=11,
        color='green'
    )
    fig.text(
        0.45, 0.03,
        f'P{len(pontos_controle) - 1}: ({end_point[0]}, {end_point[1]})',
        ha='center',
        fontsize=11,
        color='green'
    )
    fig.text(
        0.70, 0.03,
        f'P{len(pontos_controle) - 2}: ({pontos_controle[-2][0]}, {pontos_controle[-2][1]})',
        ha='center',
        fontsize=11,
        color='blue'
    )
    plt.ioff()
    plt.show(block=True)

if __name__ == "__main__":
    main()
