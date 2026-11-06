"""
Flood fill (x, y, cor, novacor):
	se (x, y) = cor
	pixel(x, y) <- novacor
	Flood fill(x+1, y, cor, nova cor)
	Flood fill(x, y-1, cor, nova cor)
	Flood fill(x-1, y, cor, nova cor)
	Flood fill(x, y+1, cor, nova cor)
"""
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def bresenham_linha(x1, y1, x2, y2):
    
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

def bresenham_circunf(xc, yc, r):

    pontos_x = []
    pontos_y = []

    x = 0
    y = r
    p = 1 - r

    while x <= y:
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

        if p >= 0:
            y = y - 1
            p = p + 2 * x - 2 * y + 5
            x = x + 1
        else:
            p = p + 2 * x + 3
            x = x + 1

    return pontos_x, pontos_y


def desenhar_retangulo(x1, y1, x2, y2):
    vertices = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
    pontos_retangulo = set()
    for indice, inicio in enumerate(vertices):
        fim = vertices[(indice + 1) % len(vertices)]
        pontos_x, pontos_y = bresenham_linha(*inicio, *fim)
        pontos_retangulo.update(zip(pontos_x, pontos_y))
    return pontos_retangulo

def desenhar_circunferencia(centro, raio):
    xc, yc = centro
    pontos_x, pontos_y = bresenham_circunf(xc, yc, raio)
    pontos_circunferencia = set(zip(pontos_x, pontos_y))
    return pontos_circunferencia

def desenhar_poligono(vertices):
    # Liga vertices consecutivos e fecha o poligono com Bresenham
    pontos_poligono = set()
    for indice, inicio in enumerate(vertices):
        fim = vertices[(indice + 1) % len(vertices)]
        pontos_x, pontos_y = bresenham_linha(*inicio, *fim)
        pontos_poligono.update(zip(pontos_x, pontos_y))
    return sorted(pontos_poligono)

def ler_ponto(nome):
    while True:
        try:
            print(f"Digite o {nome} (ex: 1,1): ", end="", flush=True)
            ponto = input().strip()
            x, y = ponto.split(",")
            return int(x.strip()), int(y.strip())
        except ValueError:
            print("Entrada invalida. Use o formato x,y, por exemplo: 1,1")


def mostrar_borda(pontos, titulo):
    # exibe qualquer conjunto de pixels gerado pelos algoritmos de Bresenham
    pontos = set(pontos)
    if not pontos:
        raise ValueError("A figura precisa ter pelo menos um ponto")

    x_coords, y_coords = zip(*pontos)
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    limite_x = range(min_x - 3, max_x + 3)
    limite_y = range(min_y - 3, max_y + 3)
    bordas_x = [valor - 0.5 for valor in range(min_x, max_x + 2)]
    bordas_y = [valor - 0.5 for valor in range(min_y, max_y + 2)]

    plt.ion() # modo interativo para permitir atualização dinâmica do gráfico
    fig, ax = plt.subplots(figsize=(7, 7))
    for x, y in pontos:
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

    ax.set_xticks(limite_x)
    ax.set_yticks(limite_y)
    ax.set_xticks(bordas_x, minor=True)
    ax.set_yticks(bordas_y, minor=True)
    ax.set_xlim(min_x - 0.5, max_x + 0.5)
    ax.set_ylim(min_y - 0.5, max_y + 0.5)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, which="minor", color="black", linewidth=0.8)
    ax.set_axisbelow(False)
    ax.set_title("Algoritmo Flood Fill - " + titulo)
    ax.set_xlabel("Coordenadas X")
    ax.set_ylabel("Coordenadas Y")
    plt.show(block=False)
    plt.pause(0.1)
    return fig, ax


def flood_fill(x, y, cor, novacor, pixels, atualizar=None):
    if y < 0 or y >= len(pixels) or x < 0 or x >= len(pixels[0]): # verifica o limite da matriz
        return
    if pixels[y][x] == cor:
        pixels[y][x] = novacor
        if atualizar is not None:
            atualizar(x, y) # se o pixel for válido, ele recebe a novacor
        flood_fill(x + 1, y, cor, novacor, pixels, atualizar) # o algoritmo segue para os quatro vizinhos
        flood_fill(x, y - 1, cor, novacor, pixels, atualizar)
        flood_fill(x - 1, y, cor, novacor, pixels, atualizar)
        flood_fill(x, y + 1, cor, novacor, pixels, atualizar)


def preencher_figura(pontos, semente, atualizar=None):
    # marca a borda, executa o flood fill e retorna borda e preenchimento
    x_coords, y_coords = zip(*pontos)
    deslocamento_x = min(x_coords) - 1
    deslocamento_y = min(y_coords) - 1
    largura = max(x_coords) - deslocamento_x + 2
    altura = max(y_coords) - deslocamento_y + 2
    pixels = [[0 for _ in range(largura)] for _ in range(altura)]

    for x, y in pontos: # percorre as coordenadas do polígono
        pixels[y - deslocamento_y][x - deslocamento_x] = 1 # translação da matriz

    semente_x = semente[0] - deslocamento_x
    semente_y = semente[1] - deslocamento_y
    def atualizar_ponto(x, y):
        if atualizar is not None:
            atualizar(x + deslocamento_x, y + deslocamento_y)

    flood_fill(semente_x, semente_y, 0, 2, pixels, atualizar_ponto)

    return {
        (x + deslocamento_x, y + deslocamento_y)
        for y, linha in enumerate(pixels)
        for x, valor in enumerate(linha)
        if valor != 0
    }


def animar_preenchimento(pontos, semente, titulo):
    fig, ax = mostrar_borda(pontos, titulo + " - preenchendo")

    def atualizar(x, y):
        if not plt.fignum_exists(fig.number):
            return
        ax.add_patch(
            Rectangle(
                (x - 0.5, y - 0.5),
                1,
                1,
                facecolor="tab:blue",
                edgecolor="tab:blue",
                zorder=2,
            )
        )
        fig.canvas.draw_idle()
        plt.pause(0.02)

    preencher_figura(pontos, semente, atualizar)
    if plt.fignum_exists(fig.number):
        ax.set_title("Algoritmo Flood Fill - " + titulo + " - preenchido")
        fig.canvas.draw_idle()
        plt.ioff()
        plt.show()



def main():
    print("\nAlgoritmo de Flood Fill")
    print(" \nDefina a figura:")
    print("\n1 Retângulo \n2 Circunferência \n3 Polígono A \n4 Polígono C \n5 Polígono livre")
    opcao = int(input("Escolha uma opção (1-5): "))
    if opcao == 1:
        print("\nDefina os cantos da extremidade do retângulo:")
        x1, y1 = ler_ponto("p1")
        x2, y2 = ler_ponto("p2")

        pontos = desenhar_retangulo(x1, y1, x2, y2)
        semente = ((x1 + x2) // 2, (y1 + y2) // 2)
        animar_preenchimento(pontos, semente, "Retângulo")

    elif opcao == 2:
        print("\nDefina o centro da circunferência:")
        xc, yc = ler_ponto("centro")

        r = int(input("Digite o raio da circunferência: "))
        pontos = desenhar_circunferencia((xc, yc), r)
        animar_preenchimento(pontos, (xc, yc), "Circunferência")

    elif opcao == 3:
        print("\nVértices do polígono A: (1, 21), (14,26), (27, 18), (23, 13), (5,11), (10, 16)")
        vertices = [(1, 21), (14,26), (27, 18), (23, 13), (5,11), (10, 16)]

        pontos = desenhar_poligono(vertices)
        centro = (
            round(sum(x for x, _ in vertices) / len(vertices)),
            round(sum(y for _, y in vertices) // len(vertices)),
        )
        animar_preenchimento(pontos, centro, "Polígono A")

    elif opcao == 4:
        print("\nVértices do polígono C: (5,20), (12,20), (15,17), (18,20), (25,20), (25,13), (15, 5), (5,13)")
        vertices = [(5,20), (12,20), (15,17), (18,20), (25,20), (25,13), (15, 5), (5,13)]

        pontos = desenhar_poligono(vertices)
        centro = (
            sum(x for x, _ in vertices) // len(vertices),
            sum(y for _, y in vertices) // len(vertices),
        )
        animar_preenchimento(pontos, centro, "Polígono C")

    elif opcao == 5:
            print("\nDefina os vértices do polígono:")
            vertices = []
            while True:
                try:
                    ponto = input("Digite um vértice (ex: 1,1) ou 'fim' para encerrar: ").strip()
                    if ponto.lower() == 'fim':
                        break
                    x, y = ponto.split(",")
                    vertices.append((int(x.strip()), int(y.strip())))
                except ValueError:
                    print("Entrada inválida. Use o formato x,y, por exemplo: 1,1")
    
            pontos = desenhar_poligono(vertices)
            centro = (
                sum(x for x, _ in vertices) // len(vertices),
                sum(y for _, y in vertices) // len(vertices),
            )
            animar_preenchimento(pontos, centro, "Polígono livre")

    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
