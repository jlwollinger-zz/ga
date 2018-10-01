import numpy as np
import math   # This will import math module
from cromossomo import Cromossomo
from cromossomo import CromossomoFactory

tamanhoPopulacao = 20
populacao = []
geracoes = 10000

if '__name__' == '__main__':
    main(cromossomos)

for i in range (0, tamanhoPopulacao):
    populacao.append(CromossomoFactory.build())

for cr in populacao:
    print(cr.genes)


def main():
    cromossomos = generateCromossomos()
    for i in range(0, geracoes):
        #cromossomos = fitness(cromossomos) #preencher a útlima coluna de aptidão
        cromossomos = selecao(cromossomos) #fazer o sort e selecionar os 10 primeiros
        cromossomos = crossover(cromossomos) #fazer o crossover
        cromossomos = mutacao(cromossomos) #sortear algum cromossomo para mutar


def fitness(cromossomos):
    for i in range(0, 20):
        for j in range(0, 20):
            cromossomos[i, j] = math.sqrt((pow(cromossomos[i + 1] - cromossomos[j]), 2) + (pow(cromossomos[i + 1] - cromossomos[j]))) 
    #dcidade(i,j)=sqrt((x(i)-x(j))^2+(y(i)-y(j))^2)


def selecao(cromossomos):

    #cromossomos = sorted(cromossomos)
    return cromossomos

def crossover(cromossomos):

    return cromossomos


def mutacao(cromossomos):

    return cromossomos
