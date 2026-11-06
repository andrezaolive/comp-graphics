"""
retorna os pontos médios dos segmentos de retas entre os pontos de controle da curva de Bézier
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def pontos_medios_quadratica(P0, P1, P2):
    P0m1 = (P0 + P1) / 2
    P1m1 = (P1 + P2) / 2
    P0m2 = (P0m1 + P1m1) / 2

    return P0m1, P1m1, P0m2


def casteljau_quadratica(P0, P1, P2, t, pontos_curva):
    if t > 0.005:
        P0m1, P1m1, P0m2 = pontos_medios_quadratica(P0, P1, P2)
        e = t / 2

        # registra o ponto médio antes de subdividir os dois lados da curva
        pontos_curva.append(P0m2)
        casteljau_quadratica(P0, P0m1, P0m2, e, pontos_curva)
        casteljau_quadratica(P0m2, P1m1, P2, e, pontos_curva)
    else:
        pontos_curva.append(P0)

def pontos_medios_cubica(P0, P1, P2, P3):
    # retorna os pontos intermediários da curva para subdivisão

    # primeira subdivisão
    P0m1 = (P0 + P1) / 2
    P1m1 = (P1 + P2) / 2
    P2m1 = (P2 + P3) / 2
    
    # segunda subdivisão
    P0m2 = (P0m1 + P1m1) / 2
    P1m2 = (P1m1 + P2m1) / 2
    
    # terceira subdivisão (ponto médio máximo)
    P0m3 = (P0m2 + P1m2) / 2
    
    return P0m1, P1m1, P2m1, P0m2, P1m2, P0m3

def casteljau_cubica(P0, P1, P2, P3, t, pontos_curva):
    # algoritmo de De Casteljau recursivo para calcular pontos da curva de Bézier

    if t > 0.005:
        e = t / 2
        P0m1, P1m1, P2m1, P0m2, P1m2, P0m3 = pontos_medios_cubica(P0, P1, P2, P3)
        # Registra o ponto médio antes de subdividir os dois lados da curva.
        pontos_curva.append(P0m3)
        casteljau_cubica(P0, P0m1, P0m2, P0m3, e, pontos_curva)
        casteljau_cubica(P0m3, P1m2, P2m1, P3, e, pontos_curva)
    else:
        pontos_curva.append(P0)
    return np.array(pontos_curva)

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
    print("Algoritmo Casteljau para curvas cúbicas de Bézier")
    print("\nEscolha o tipo de curva que deseja desenhar:")
    print("\n1 Curva com 3 pontos (Quadrática); \n2 Curva com 4 pontos (Cúbica); \n3 Sair")
    opcao = int(input("\nEscolha uma opção (1-3): "))
    if opcao == 1:
        funcao_curva = casteljau_quadratica
        pontos_controle = [
            ler_ponto("P0"),
            ler_ponto("P1"),
            ler_ponto("P2"),
        ]
    elif opcao == 2:
        funcao_curva = casteljau_cubica
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
    pontos_curva = []
    funcao_curva(*pontos_controle, 1, pontos_curva)
    # inclui o último ponto de controle para a animação terminar no fim da curva
    pontos_curva.append(pontos_controle[-1])
    pontos_curva = np.array(pontos_curva)

    x_coords = np.rint(pontos_curva[:, 0]).astype(int) # discretiza e gera recursao
    y_coords = np.rint(pontos_curva[:, 1]).astype(int)
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
    ax.set_title('Algoritmo Casteljau para Curvas de Bézier')
    ax.set_xlabel('Coordenadas X')
    ax.set_ylabel('Coordenadas Y')
    fig.subplots_adjust(bottom=0.16)

    # desenha cada ponto médio arredondado como um pixel, um de cada vez
    plt.ion()
    plt.show(block=False)
    pixels = list(dict.fromkeys(zip(x_coords, y_coords)))
    pixel_final = tuple(np.rint(pontos_controle[-1]).astype(int))
    if pixels[0] != pixel_final:
        if pixel_final in pixels:
            pixels.remove(pixel_final)
        pixels.append(pixel_final)

    pixels_plotados = set()
    for x, y in pixels:
        # um pixel repetido não precisa ser desenhado novamente
        if (x, y) in pixels_plotados:
            continue

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
        pixels_plotados.add((x, y))
        fig.canvas.draw_idle()
        fig.canvas.flush_events()
        plt.pause(0.01)

    # legendas
    start_point = pontos_controle[0]
    end_point = pontos_controle[-1]
    ax.plot(start_point[0], start_point[1], color='green', marker='o', markersize=10, zorder=5)
    ax.plot(end_point[0], end_point[1], color='green', marker='o', markersize=10, zorder=5)
    ax.plot(pontos_controle[-2][0], pontos_controle[-2][1], color='blue', marker='o', markersize=10, zorder=5)
    if funcao_curva == casteljau_cubica:
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
