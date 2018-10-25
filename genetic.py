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
        populacao.append(CromossomoFactory().build()) #Gera uma população de 20 cromossomos e adiciona no array de população
    return populacao

def main():
    populacao = generatePopulacao() #Gera a população
    for _ in range(0, geracoes):
        populacao = fitness(populacao) #preencher a útlima coluna de aptidão
        populacao = selecao(populacao) #fazer o sort e selecionar os 10 primeiros
        populacao = crossover(populacao) #fazer o crossover
        populacao = mutacao(populacao) #sortear algum cromossomo para mutar

    
    #Imprimi os resultados
    print("Tamanho da populução: ", len(populacao))
    print("Taxa de mutação: ", Taxa_de_mutacao)
    print("Número de cidades: ", len(populacao[0].genes))
    print("Melhor custo: ", populacao[0].aptidao)
    print("Melhor genes:", populacao[0].genes)

    plt.plot(populacao[0].genes)#, '-ok') #TODO: Este é o gráfico certo? não achei o ideal
    plt.show()


def fitness(populacao):
    for x in range(0, 20):
        distancias = [[0 for x in range(20)] for y in range(20)]  #inicia a matriz de distâncias
        cromossomoIterado = populacao[x] # pega o cromossomo a ser calculado
        for i in range(0, 20):
            cromossomoIterado.genes[ULTIMO_GENE] = cromossomoIterado.genes[i] #o último tem que ser igual ao primeiro para fechar o ciclo
            for j in range(0, 20):
                distancias[i][j] = cromossomoIterado.genes[i] - cromossomoIterado.genes[j] #calcula a distancia e armazena na matriz

        distanciaCromossomo = [0 for x in range(20)] #inicia o array de distancias do cromossomo
        for i in range(0,20):
            for j in range(0,20):
                distanciaCromossomo[i] += distancias[i][j] #Soma as distâncias e armazena no array

        distanciaCromossomo.sort(key=lambda x: x) #Ordena pelas distâncias, da menor para a maior
        cromossomoIterado.aptidao = distanciaCromossomo[0] #Atribui a menor distância para o atributo "aptidao"


    return populacao #TODO: A melhor aptidão sempre está dando negativo, será que está certo isso?

def selecao(populacao):
    populacao.sort(key=lambda x: x.aptidao) #Ordena pela aptidao, da maior para a menor 
    return populacao

def crossover(populacao):
    metade_da_metade = 5
    for i in range(0, metade_da_metade): #Itera cinco vezes gerando 10 filhos
        pai = populacao[i] #Para o pai, pega-se o primeiro(melhor) cromossomo
        mae = populacao[randrange(0, 10)] #Para o outro pai, pega-se um cromossomo aleartório
        filho1 = Cromossomo()
        filho1.genes = pai.crossover(mae)  #Realiza o crossover

        filho2 = Cromossomo()
        filho2.genes = mae.crossover(pai) #Realiza o crossover
        
        populacao[i + 10] = filho1 #Atribui os filhos
        populacao[i + 11] = filho2

    return populacao


def mutacao(populacao):
    prob = randrange(0, 100) #Sorteia-se um número de 0 a 100, se for igual ou menor a 5, faz a mutação
    if prob <= 5: #   
        global Taxa_de_mutacao
        Taxa_de_mutacao = Taxa_de_mutacao + 1
        for i in range(10, 20): 
            geneX = randrange(0, 20) #Sorteia-se um gene para trocar
            geneY = randrange(0, 20) #Sorteia-se outro gene para trocar com o primeiro
            valor_a_trocar = populacao[i].genes[geneX] 
            populacao[i].genes[geneX] = populacao[i].genes[geneY] #Realiza a troca
            populacao[i].genes[geneY] = valor_a_trocar #Realiza a troca
    return populacao




main()