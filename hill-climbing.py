import math
import random


def calcular_distancia_euclidiana(cidade_atual, proxima_cidade):
    """
    Calcula a distância entre duas cidades a partir da distância euclidiana
    """
    x1, y1 = cidade_atual
    x2, y2 = proxima_cidade
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def selecionar_caminho_aleatorio(cidades):
    """
    Dado um vetor de cidades com coordenadas (x, y), embaralha as cidades aleatoriamente
    e retorna como um novo caminho
    """
    random.shuffle(cidades)
    return cidades


def calcular_distancia_do_caminho(cidades):
    """
    Dado um vetor de cidades que represente o caminho, é calculado a distancia total do caminho
    calculando a distância euclidiana entre as cidades
    """
    distancia_total = 0
    numero_de_cidades = len(cidades)
    for i in range(numero_de_cidades):
        cidade_atual = cidades[i]
        proxima_cidade = cidades[(i + 1) % numero_de_cidades]
        distancia = calcular_distancia_euclidiana(cidade_atual, proxima_cidade)
        distancia_total += distancia
    return distancia_total

def gerar_vizinho(cidades):
    """
    Dado um vetor de vidades que represente o caminho, é gerado um novo caminho trocando a posição
    de duas cidades aleatórias.
    """
    vizinho = cidades.copy()

    indice_aleatorio_1 = random.randint(0, len(cidades) - 1)
    indice_aleatorio_2 = random.randint(0, len(cidades) - 1)

    auxiliar = vizinho[indice_aleatorio_1]
    vizinho[indice_aleatorio_1] = vizinho[indice_aleatorio_2]
    vizinho[indice_aleatorio_2] = auxiliar

    return vizinho


def gerar_vizinhos(cidades, numero_de_vizinhos):
    """
    Dado um vetor de cidades que represente o caminho e o número de vizinhos, gera n vizinhos usando
    o algoritmo troca-2
    """
    vizinhos = []
    for i in range(numero_de_vizinhos):
        vizinho = gerar_vizinho(cidades)
        vizinhos.append(vizinho)
    return vizinhos


def selecionar_menor_vizinho(vizinhos):
    """
    Dado um vetor de vizinhos, calcula a distância de cada vizinho, procura e retorna a menor distância
    """
    menor_vizinho = vizinhos[0]
    menor_distancia_do_vizinho = calcular_distancia_do_caminho(menor_vizinho)

    for i in range(1, len(vizinhos)):
        distancia_do_vizinho = calcular_distancia_do_caminho(vizinhos[i])
        if distancia_do_vizinho < menor_distancia_do_vizinho:
            menor_vizinho = vizinhos[i]
            menor_distancia_do_vizinho = distancia_do_vizinho

    return menor_vizinho, menor_distancia_do_vizinho

def hill_climbing(cidades, iteracoes, numero_de_vizinhos):
    menor_caminho = cidades.copy()
    menor_distancia = calcular_distancia_do_caminho(menor_caminho)

    for i in range(iteracoes):
        caminho = selecionar_caminho_aleatorio(cidades.copy())
        distancia = calcular_distancia_do_caminho(caminho)

        while True:
            vizinhos = gerar_vizinhos(caminho.copy(), numero_de_vizinhos)
            vizinho, distancia_do_vizinho = selecionar_menor_vizinho(vizinhos)

            if distancia_do_vizinho < distancia:
                caminho = vizinho.copy()
                distancia = distancia_do_vizinho
            else:
                break

        if distancia < menor_distancia:
            menor_caminho = caminho.copy()
            menor_distancia = distancia

    return menor_caminho, menor_distancia


def ler_arquivo(nome_arquivo):
    cidades = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            dados = linha.split()
            identificador = int(dados[0])
            coordenada_x = float(dados[1])
            coordenada_y = float(dados[2])
            cidade = (coordenada_x, coordenada_y)
            cidades.append(cidade)
    return cidades


nome_arquivo = 'data/att48.tsp.txt'
cidades = ler_arquivo(nome_arquivo)

caminho, distancia = hill_climbing(cidades, iteracoes=1000, numero_de_vizinhos=1000)

print("Caminho: ", caminho)
print("Distância: ", distancia)
