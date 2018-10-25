from random import randrange
import numpy as np

class Cromossomo:
    genes = []
    aptidao = 0
    
    def crossover(self, mae):
        genes = [0 for x in range(21)]
        for _ in range(0, 10): #10 trocas
            n_troca = randrange(1, 19) #Gera-se um número aleatório de 1 até 19 para ser o índice do gene a ser trocado
            genes[n_troca] = mae.genes[n_troca] #Realiza a troca
        for i in range(0,20):
            if(genes[i] == 0):
                genes[i] = self.genes[i] #Preenche os genes restantes com os genes do pai

        return genes


class CromossomoFactory:
    #Inicializa-se o cromossomo e seus atributos
    @staticmethod
    def build():
        crom = Cromossomo()
        crom.genes = np.random.uniform(low=00, high=1, size=(21,)) #Gera os genes aleatóriamente de 0 até 1 
        crom.aptidao = 0
        crom.genes[20] = crom.genes[0]
        return crom