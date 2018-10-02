import numpy as np
import math   # This will import math module
from cromossomo import Cromossomo
from cromossomo import CromossomoFactory
from random import randrange

tamanhoPopulacao = 20
populacao = []
geracoes = 10000

def generatePopulacao():
    for i in range (0, tamanhoPopulacao):
        populacao.append(CromossomoFactory().build())
    return populacao

print(generatePopulacao())
def main():
    populacao = generatePopulacao()
    for i in range(0, geracoes):
        #populacao = fitness(populacao) #preencher a útlima coluna de aptidão
        populacao = selecao(populacao) #fazer o sort e selecionar os 10 primeiros
        populacao = crossover(populacao) #fazer o crossover
        populacao = mutacao(populacao) #sortear algum cromossomo para mutar

    #plotar gráfico


def fitness(populacao):
    for i in range(0, 20):
        for j in range(0, 20):
            populacao[i, j] = math.sqrt((pow(populacao[i + 1] - populacao[j]), 2) + (pow(populacao[i + 1] - populacao[j]))) 
    #dcidade(i,j)=sqrt((x(i)-x(j))^2+(y(i)-y(j))^2)

def selecao(populacao):
    populacao.sort(key=lambda x: populacao.aptidao)
    for x in range(10):
        populacao.pop()
    return populacao

def crossover(populacao):
    metade = 10
    
    return populacao


def mutacao(populacao):
    prob = randrange(0, 100)
    if prob =< 5: #O operador de mutação atua sobre        
        print("MUTEI") #cada membro da nova geração (10 últimos) com probabilidade de 0,05
        for i in range(10, 20): 
            geneX = randrange(0, 20) 
            geneY = randrange(0, 20)
            valorATrocar = populacao[i].cromossomo.genes[geneX]
            populacao[i].cromossomo.genes[geneX] = populacao[i].cromossomo.genes[geneY]
            populacao[i].cromossomo.genes[geneY] = valorATrocar
    return populacao




main()