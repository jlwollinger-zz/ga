import numpy as np
import math
from cromossomo import Cromossomo
from cromossomo import CromossomoFactory
from random import randrange
from matplotlib import pyplot as plt
from matplotlib.path import Path

tamanhoPopulacao = 20
populacao = []
geracoes = 100#0#0
ULTIMO_GENE = 20
Taxa_de_mutacao = 0


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

    
    print("Tamanho da populução: ", len(populacao))
    print("Taxa de mutação: ", Taxa_de_mutacao)
    print("Número de cidades: ", len(populacao[0].genes))
    print("Melhor custo: ", populacao[0].aptidao)
    print("Melhor solução:", populacao[0].genes)

    plt.plot(populacao[0].genes, '-ok') #TODO: Este é o gráfico certo? não achei o ideal
    plt.show()


def fitness(populacao):
    for x in range(0, 20):
        distancias = [[0 for x in range(20)] for y in range(20)] 
        cromossomoIterado = populacao[x]
        for i in range(0, 20):
            cromossomoIterado.genes[ULTIMO_GENE] = cromossomoIterado.genes[i] #o último tem que ser igual ao primeiro para fechar o ciclo
            for j in range(0, 20):
                distancias[i][j] = cromossomoIterado.genes[i] - cromossomoIterado.genes[j]

        distanciaCromossomo = [0 for x in range(20)]
        for i in range(0,20):
            for j in range(0,20):
                distanciaCromossomo[i] += distancias[i][j]

        distanciaCromossomo.sort(key=lambda x: x)                            
        cromossomoIterado.aptidao = distanciaCromossomo[0]


    return populacao #TODO: A melhor aptidão sempre está dando negativo, será que está certo isso?

def selecao(populacao):
    populacao.sort(key=lambda x: x.aptidao)
    #for _ in range(10):
        #populacao.pop()
    return populacao

def crossover(populacao):
    metade_da_metade = 5
    for i in range(0, metade_da_metade):
        pai = populacao[i]
        mae = populacao[randrange(0, 10)]
        filho1 = Cromossomo
        filho1.genes = pai.crossover(mae) #TODO: filho está ficanco igual ao pai. Não consegui descobrir ainda o porque
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
        global Taxa_de_mutacao   #cada membro da nova geração (10 últimos) com probabilidade de 0,05
        Taxa_de_mutacao = Taxa_de_mutacao + 1
        for i in range(10, 20): 
            geneX = randrange(0, 20) 
            geneY = randrange(0, 20)
            valor_a_trocar = populacao[i].genes[geneX]
            populacao[i].genes[geneX] = populacao[i].genes[geneY]
            populacao[i].genes[geneY] = valor_a_trocar
    return populacao




main()