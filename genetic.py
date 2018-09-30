

populacao = 20
agentes = []
geracoes = 10000


def main():
    for i in range(0, geracoes):
        agentes = fitness(agentes) #preencher a útlima coluna de aptidão
        agentes = selecao(agentes) #fazer o sort e selecionar os 10 primeiros
        agentes = crossover(agentes) #fazer o crossover
        agentes = mutacao(agentes) #sortear algum cromossomo para mutar



def fitness(agentes):
    
    return agentes

def selecao(agentes):

        #agentes = sorted(agentes)
    return agentes

def crossover(agentes):

    return agentes


def mutacao(agentes):

    return agentes
