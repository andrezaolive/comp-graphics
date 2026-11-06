## 📐 Algoritmos Fundamentais de Computação Gráfica 2D

![Math](https://img.shields.io/badge/Python-math-3776AB?&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=plotly&logoColor=white)


Este repositório contém cinco trabalhos relacionados à rasterização, preenchimento e recorte de formas digitais, implementados em Python utilizando bibliotecas como NumPy e Matplotlib.
---


### 1. 📏 Rasterização de linhas

* **Método analítico:**  
O método analítico baseia-se diretamente na equação matemática explícita da reta – y 
= mx + b – e a partir de dois pontos conhecidos percorre cada coordenada inteira de x entre os pontos, resolve a equação da reta e encontra o valor de y.

* **Método DDA (Digital Differential Analyzer):**  
O algoritmo DDA (Analisador Diferencial Digital) resolve o problema da continuidade ao alternar o eixo de controle principal com base na inclinação da reta, além de acumular o incremento de forma aditiva (y = y + incremento ou x = x + incremento), o que elimina as multiplicações do método analítico original.

* **Algoritmo Bresenham:**  
Este algoritmo decide se o próximo pixel vai ter coordenadas (x + 1, y) ou (x + 1, y + 1). Assim, ele avalia se a linha passa acima ou abaixo do ponto médio (x + 1, y + ½) e faz a conversão de segmentos de reta contínuos em uma grade discreta de pixels utilizando aritmética inteira, sem operações em ponto flutuante.

### 2. ⭕ Rasterização de circunferências

* **Método da equação paramétrica:**  
O método da equação paramétrica calcula o desenho de circunferências utilizando as 
funções trigonométricas de seno e cosseno baseadas em um parâmetro angular. 

* **Método incremental por simetria:**  
O método incremental por simetria resolve o desenho eficiente de circunferências ao 
aproveitar as propriedades geométricas de espelhamento e calcular os pixels por meio de 
diferenças incrementais. O algoritmo calcula os pixels referentes a apenas um oitavo 
da circunferência (do ângulo de 0° a 45°) e os demais sete octantes são preenchidos por reflexão simétrica.

* **Algoritmo Bresenham:**   
Este algoritmo faz o desenho de circunferências aproveitando a simetria de 8 vias (octantes) do método incremental, mas utiliza exclusivamente aritmética de números inteiros e explorando a comparação do ponto médio.

### 3. 🎨 Preenchimento de polígonos

* **Algoritmo Flood Fill:**  
Este algoritmo faz a identificação de regiões internas de polígonos simples e complexos através do cálculo de interseções horizontais e verticais, além de verificação de cores. 

* **Scanline:**  
O método de varredura por linhas de escaneamento resolve o problema de preencher polígonos complexos ao analisar as intersecções geométricas entre as arestas da figura e as linhas horizontais da tela. 

### 4. 〰️ Curvas de Bézier

* **Método da equação paramétrica:**  
Este método faz o mapeamento de trajetórias suaves a partir de pontos de controle, parâmetro t e polinômios de Bernstein. Implementação feita para curvas quadráticas (3 pontos) e cúbicas (4 pontos).

* **Casteljau:**  
O método de Casteljau realiza etapas de cálculo do ponto médio entre os pontos de controle, de modo que cada etapa reduz o número de pontos intermediários em um até obter um único ponto final sobre a curva, fazendo recursivamente até encontrar a profundidade adequada de rasterização de pixels. Implementação feita para curvas quadráticas (3 pontos) e cúbicas (4 pontos).


### 5. ✂️ Recorte de polígonos
* **Algoritmo Sutherland-Hodgman:**  
Faz o processamento em *pipeline* de 4 etapas independentes (esquerda, inferior, direita e superior) avaliando os 4 casos de recorte de arestas e transformação de vértices em relação às bordas da janela de visualização.

---

## 🛠️ Tecnologias Utilizadas

* **Language:** Python 3.13
* **Suporte:** Math
* **Vector Algebra:** NumPy
* **Visualization:** Matplotlib
---
Este repositório oferece uma abordagem prática e educacional para a rasterização e preenchimento de linhas e formas 2D utilizando conceitos fundamentais da computação gráfica.