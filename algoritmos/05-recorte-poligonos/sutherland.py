'''
CASO 1: um dos dois vértices é adicionado à lista de saídas (p, no caso).
CASO 2: o ponto “i” de interseção é tratado como um vértice de saída (a ser traçado).
CASO 3: os dois vértices são descartados.
CASO 4: os dois pontos “i” e “p” são colocados na lista de vértices de saída.
'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# verifica se o ponto está dentro da janela em relação à aresta atual
def ponto_dentro(ponto, perimetro, xmin, ymin):
    x, y = ponto
    aresta_x1, aresta_y1, aresta_x2, aresta_y2 = perimetro

    return (x >= aresta_x1 if aresta_x1 == xmin else x <= aresta_x1) if aresta_x1 == aresta_x2 else (y >= aresta_y1 if aresta_y1 == ymin else y <= aresta_y1)


# calcula onde a aresta do polígono cruza a aresta da janela de recorte
def intersecao(p1, p2, perimetro):
    x1, y1 = p1
    x2, y2 = p2
    aresta_x1, aresta_y1, aresta_x2, aresta_y2 = perimetro

    if aresta_x1 == aresta_x2:
        x_int = aresta_x1
        t = (x_int - x1) / (x2 - x1)
        y_int = y1 + t * (y2 - y1)
    else:
        y_int = aresta_y1
        t = (y_int - y1) / (y2 - y1)
        x_int = x1 + t * (x2 - x1)

    return (x_int, y_int)


# recorta o polígono contra os quatro lados da janela pelo algoritmo de Sutherland-Hodgman
def sutherland(poligono, reta_recorte):
    x_min, x_max, y_min, y_max = reta_recorte
    perimetros = [
        (x_min, y_min, x_min, y_max),  # esquerda
        (x_min, y_max, x_max, y_max),  # superior
        (x_max, y_max, x_max, y_min),  # direita
        (x_max, y_min, x_min, y_min)   # inferior
    ]

    poligono_recortado = poligono[:]
    for perimetro in perimetros:
        # não há vértices para processar se o polígono já ficou totalmente fora
        if not poligono_recortado:
            break

        novo_poligono = []
        ponto_anterior = poligono_recortado[-1]
        for ponto_atual in poligono_recortado:
            # adiciona interseções e vértices conforme cada ponto cruza ou fica dentro da janela
            if ponto_dentro(ponto_atual, perimetro, x_min, y_min):
                if not ponto_dentro(ponto_anterior, perimetro, x_min, y_min):
                    intersec = intersecao(ponto_anterior, ponto_atual, perimetro)
                    novo_poligono.append(intersec)
                novo_poligono.append(ponto_atual)
            elif ponto_dentro(ponto_anterior, perimetro, x_min, y_min):
                intersec = intersecao(ponto_anterior, ponto_atual, perimetro)
                novo_poligono.append(intersec)
            ponto_anterior = ponto_atual
        poligono_recortado = novo_poligono

    return poligono_recortado


# anima o polígono original e o resultado após recortar cada aresta da janela
def animar_poligono(poligono, xmin, xmax, ymin, ymax, nome, cor):
    etapas = [("Polígono original", poligono)]
    poligono_atual = poligono[:]
    arestas = [
        ("Recorte pela aresta direita", "direita"),
        ("Recorte pela aresta inferior", "inferior"),
        ("Recorte pela aresta esquerda", "esquerda"),
        ("Recorte pela aresta superior", "superior"),
    ]

    for descricao, aresta in arestas:
        if poligono_atual:
            xs = [ponto[0] for ponto in poligono_atual]
            ys = [ponto[1] for ponto in poligono_atual]
            margem = max(max(xs) - min(xs), max(ys) - min(ys), 1) + 1
            limite_direito = max(xs) + margem
            limite_esquerdo = min(xs) - margem
            limite_inferior = min(ys) - margem
            limite_superior = max(ys) + margem

            # mantém as outras bordas fora do polígono para aplicar só a aresta atual
            if aresta == "esquerda":
                janela_etapa = (xmin, limite_direito, limite_inferior, limite_superior)
            elif aresta == "superior":
                janela_etapa = (limite_esquerdo, limite_direito, limite_inferior, ymax)
            elif aresta == "direita":
                janela_etapa = (limite_esquerdo, xmax, limite_inferior, limite_superior)
            else:
                janela_etapa = (limite_esquerdo, limite_direito, ymin, limite_superior)

            poligono_atual = sutherland(poligono_atual, janela_etapa)

        etapas.append((descricao, poligono_atual[:]))

    fig, ax = plt.subplots()

    def update(frame):
        # limpa e redesenha a cena em cada etapa da animação
        ax.clear()
        ax.set_xlim(-50, 550)
        ax.set_ylim(-50, 550)
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])

        # desenha a área de recorte
        ax.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'k-', linewidth=2, label="Região de recorte")

        descricao, poligono_etapa = etapas[frame]
        ax.set_title(descricao)
        if poligono_etapa:
            pontos_x, pontos_y = zip(*(poligono_etapa + [poligono_etapa[0]]))
            ax.fill(pontos_x, pontos_y, facecolor=cor, edgecolor='black',
                    linewidth=2, alpha=0.7, label=f'Polígono {nome.upper()}')

        ax.legend()

    ani = animation.FuncAnimation(fig, update, frames=5, interval=2000, repeat=False)
    plt.show()


# apresenta as opções e inicia o recorte somente do polígono escolhido
def main():
    print("Recorte de polígonos com Sutherland-Hodgman:")
    print("\n 1(a) Triângulo \n 2(b) Pentágono \n 3(c) Octógono \n 4(d) Hexágono")
    opcao = int(input("\nEscolha um polígono para recortar (1-4): "))

    # definição dos polígonos
    poligonos = {
        1: ("a", "Triângulo", [[200, 200], [200, 500], [500, 200]], "green"),
        2: ("b", "Pentágono", [[90, 200], [250, 200], [340, 345], [170, 470], [20, 345]], "red"),
        3: ("c", "Octógono", [[120, 320], [120, 480], [380, 480], [380, 340], [300, 340],
                                [300, 410], [200, 410], [200, 320]], "yellow"),
        4: ("d", "Hexágono", [[150, 100], [150, 150], [200, 150], [200, 200], [300, 200], [300, 150],
                                [350, 150], [350, 100], [350, 50], [300, 50], [300, 0], [200, 0],
                                [200, 50], [150, 50]], "blue"),
    }

    if opcao not in poligonos:
        print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
        return

    # envia à animação apenas os dados do polígono selecionado
    nome, descricao, vertices, cor = poligonos[opcao]
    print(f"\nVértices do {descricao.lower()}: {vertices}")

    xmin, ymin, xmax, ymax = 100, 100, 400, 400                   # janela de recorte
    animar_poligono(vertices, xmin, xmax, ymin, ymax, nome, cor)


if __name__ == "__main__":
    main()
