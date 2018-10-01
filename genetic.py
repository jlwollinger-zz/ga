import numpy as np
import math   # This will import math module
from cromossomo import Cromossomo
from cromossomo import CromossomoFactory
from random import randrange

tamanhoPopulacao = 20
populacao = []
geracoes = 10000

def generateCromossomos():
    for i in range (0, tamanhoPopulacao):
        populacao.append(CromossomoFactory().build())
    return populacao

print(generateCromossomos())
def main():
    populacao = generateCromossomos()
    for i in range(0, geracoes):
        #cromossomos = fitness(cromossomos) #preencher a útlima coluna de aptidão
        populacao = selecao(populacao) #fazer o sort e selecionar os 10 primeiros
        populacao = crossover(populacao) #fazer o crossover
        populacao = mutacao(populacao) #sortear algum cromossomo para mutar

    #plotar gráfico


def fitness(cromossomos):
    for i in range(0, 20):
        for j in range(0, 20):
            cromossomos[i, j] = math.sqrt((pow(cromossomos[i + 1] - cromossomos[j]), 2) + (pow(cromossomos[i + 1] - cromossomos[j]))) 
    #dcidade(i,j)=sqrt((x(i)-x(j))^2+(y(i)-y(j))^2)


def selecao(cromossomos):

    #cromossomos = sorted(cromossomos)
    return cromossomos

def crossover(cromossomos):
    metade = 10
    
    return cromossomos


def mutacao(populacao):
    
    prob = randrange(0,100)
    if(prob < 5):
        print("MUTEI") #O operador de mutação atua sobre cada membro da nova geração com probabilidade de 0,05
        for i in range(10, 20):
            
        populacao[]

    return populacao




main()