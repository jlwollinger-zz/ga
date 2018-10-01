import numpy as np
import math   # This will import math module

populacao = 20
cromossomos = []
geracoes = 10000


if '__name__' == '__main__':
    main(cromossomos)


def main(cromossomos):
    for i in range(0, geracoes):
        cromossomos = fitness(cromossomos) #preencher a útlima coluna de aptidão
        cromossomos = selecao(cromossomos) #fazer o sort e selecionar os 10 primeiros
        cromossomos = crossover(cromossomos) #fazer o crossover
        cromossomos = mutacao(cromossomos) #sortear algum cromossomo para mutar



def fitness(cromossomos):
    x, y = 0
    cromossomos[20, x] = math.sqrt((pow(cromossomos[x + 1] - cromossomos[x]), 2) + (pow(cromossomos[y + 1] - cromossomos[y]))) 

    return cromossomos

def selecao(cromossomos):

    #cromossomos = sorted(cromossomos)
    return cromossomos

def crossover(cromossomos):

    return cromossomos


def mutacao(cromossomos):

    return cromossomos
