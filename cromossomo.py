from random import randrange
import numpy as np
class Cromossomo:
    genes = []
    aptidao = 0
    
    def crossover(self, mae):
        filho = CromossomoFactory().build()
        filho.genes = self.genes
        for _ in range(0, 10): #10 trocas
            n_troca = randrange(0, 20)
            filho.genes[n_troca] = mae.genes[n_troca]
            #print(filho.genes[n_troca])
            #print(mae.genes[n_troca])

        return filho


class CromossomoFactory:
    
    @staticmethod
    def build():
        crom = Cromossomo()
        crom.genes =  np.random.uniform(low=00, high=1, size=(21,))#random.sample(range(1 , 1000), 20)
        crom.aptidao = 0
        crom.genes[20] = crom.genes[0]
        return crom