import random
import numpy as np
class Cromossomo:
    genes = []
    aptidao = 0
    

class CromossomoFactory:

    def build():
        crom = Cromossomo
        crom.genes =  np.random.uniform(low=00, high=1, size=(20,))#random.sample(range(1 , 1000), 20)
        crom.aptidao = 0
        return crom