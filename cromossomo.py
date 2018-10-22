from random import randrange
import numpy as np
class Cromossomo:
    genes = []
    aptidao = 0
    
    def crossover(self, mae):
        genes = [0 for x in range(20)]
        for _ in range(0, 10): #10 trocas
            n_troca = randrange(1, 19) #Não troca-se o primeiro nem o último
            genes[n_troca] = mae.genes[n_troca]
        for i in range(0,20):
            if(genes[i] == 0):
                genes[i] = self.genes[i]

        return genes


class CromossomoFactory:
    
    @staticmethod
    def build():
        crom = Cromossomo()
        crom.genes =  np.random.uniform(low=00, high=1, size=(21,))#random.sample(range(1 , 1000), 20)
        crom.aptidao = 0
        crom.genes[20] = crom.genes[0]
        return crom