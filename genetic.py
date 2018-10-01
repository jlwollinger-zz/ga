import numpy as np
import math   # This will import math module

populacao = 20
agentes = []
geracoes = 10000


if '__name__' == '__main__':
    main(agentes)


def main(agentes):
    for i in range(0, geracoes):
        agentes = fitness(agentes) #preencher a útlima coluna de aptidão
        agentes = selecao(agentes) #fazer o sort e selecionar os 10 primeiros
        agentes = crossover(agentes) #fazer o crossover
        agentes = mutacao(agentes) #sortear algum cromossomo para mutar



def fitness(agentes):
    x, y = 0
    agentes[20, x] = math.sqrt((pow(agentes[x + 1] - agentes[x]), 2) + (pow(agentes[y + 1] - agentes[y]))) 

    return agentes

def selecao(agentes):

    #agentes = sorted(agentes)
    return agentes

def crossover(agentes):

    return agentes


def mutacao(agentes):

    return agentes
