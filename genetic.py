import numpy as np
import math   # This will import math module
from cromossomo import Cromossomo
from cromossomo import CromossomoFactory
from random import randrange
from matplotlib import pyplot as plt

tamanhoPopulacao = 20
populacao = []
geracoes = 10#000
ULTIMO_GENE = 20


def generatePopulacao():
    for _ in range (0, tamanhoPopulacao):
        populacao.append(CromossomoFactory().build())
    return populacao

def main():
    populacao = generatePopulacao()
    for _ in range(0, geracoes):
        populacao = fitness(populacao) #preencher a útlima coluna de aptidão
        populacao = selecao(populacao) #fazer o sort e selecionar os 10 primeiros
        populacao = crossover(populacao) #fazer o crossover
        populacao = mutacao(populacao) #sortear algum cromossomo para mutar

    print(populacao)

    plt.plot(populacao[0].genes, '-ok')
    plt.show()
    #plotar gráfico


def fitness(populacao):
    for x in range(0, 20):
        distancias = [[0 for x in range(20)] for y in range(20)] 
        cromossomoIterado = populacao[x]
        for i in range(0, 20):
            cromossomoIterado.genes[ULTIMO_GENE] = cromossomoIterado.genes[i] #o último tem que ser igual ao primeiro para fechar o clico
            for j in range(0, 20):
                distancias[i][j] = cromossomoIterado.genes[i] - cromossomoIterado.genes[j]

        distanciaCromossomo = [0 for x in range(20)]
        for i in range(0,20):
            for j in range(0,20):
                distanciaCromossomo[i] += distancias[i][j]

        distanciaCromossomo.sort(key=lambda x: x)                            
        cromossomoIterado.aptidao = distanciaCromossomo[0]


    return populacao

def selecao(populacao):
    populacao.sort(key=lambda x: x.aptidao)
    #for _ in range(10):
        #populacao.pop()
    return populacao

def crossover(populacao):
    metade_da_metade = 5
    for i in range(0 , metade_da_metade):
        pai = populacao[i]
        mae = populacao[randrange(0, 10)]
        filho1 = pai.crossover(mae)
        #print(filho1.genes)
        #print(pai.genes)
        filho2 = mae.crossover(pai)
        #print(filho2.genes)
        #print(mae.genes)
        populacao[i + 10] = filho1
        populacao[i + 11] = filho2

    return populacao


def mutacao(populacao):
    prob = randrange(0, 100)
    if prob <= 5: #O operador de mutação atua sobre        
        print("MUTEI") #cada membro da nova geração (10 últimos) com probabilidade de 0,05
        for i in range(10, 20): 
            geneX = randrange(0, 20) 
            geneY = randrange(0, 20)
            valor_a_trocar = populacao[i].genes[geneX]
            populacao[i].genes[geneX] = populacao[i].genes[geneY]
            populacao[i].genes[geneY] = valor_a_trocar
    return populacao




main()