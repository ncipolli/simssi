# intersessão em X

import random

class SinalOtimizado:
    def __init__(self):        
        pass

#recebe volumeAnt
    def gerarDados(self):
        self.volumeInicial = random.sample(range(1, 50), 4)

        self.volumeAnt = random.sample(range(10, 50), 4)

        #loop
        self.volumeProx = random.sample(range(1, 10), 4)

        volume = [val1 + val2 for val1, val2 in zip(self.volumeAnt, self.volumeProx)]

        condicao = random.choices(['pedestre', 'viatura', 'emergencia', 'nenhum'], [7, 5, 3, 10], k=4)

        return volume, condicao

# calculos
    #tempo fixo

    #tempo real
    #func não recebe arg volume vo tranca o curso
    def calculoCiclo(self, volume):

        self.pesoA = 5
        self.pesoB = 3

        self.statusA = 'amarelo'
        self.statusB = 'amarelo'
        #self.volume = random.sample(range(10, 50), 4)
    
    # definição de ciclos
    
        #valor a ser considerado na definição dos ciclos
        self.val_um = volume[0] + self.pesoA
        self.val_dois = volume[1] + self.pesoB
        self.val_tres = volume[2] + self.pesoA
        self.val_quatro = volume[3] + self.pesoB

        self.valA = self.val_um + self.val_tres
        self.valB = self.val_dois + self.val_quatro

        if self.valA > self.valB:
            statusA = 'verde'
            statusB = 'vermelho'
        elif self.valB > self.valA:
            statusB = 'verde'
            statusA = 'vermelho'

        #elif self.valA == self.valB:
        #   aqui considera as condições

        else:
            statusA = 'amarelo'
            statusB = 'amarelo'

        # considerar interação de emergência com a interface do usuário

        return statusA, statusB


    #definir volumeAnt
    #volumeAnt = [valA - valB for valA, valB in zip(volume, subtr)]

    
# atribuição de valores
# isso pode ser gerado diretamente na interface
    def atribuicaoValores(self, volume, condicao, statusA, statusB):

        self.av_um = [volume[0], condicao[0],  statusA]
        self.av_dois = [volume[1], condicao[1], statusB]
        self.av_tres = [volume[2], condicao[2], statusA]
        self.av_quatro = [volume[3], condicao[3], statusB]

        return self.av_um, self.av_dois, self.av_tres, self.av_quatro
        

sinalOtimizado = SinalOtimizado()
volume, condicao = sinalOtimizado.gerarDados()
statusA, statusB = sinalOtimizado.calculoCiclo(volume)
val1, val2, val3, val4 = sinalOtimizado.atribuicaoValores(volume, condicao, statusA, statusB)

if __name__ == '__main__':
    #print(sinalOtimizado.atribuicaoValores(volume, condicao, statusA, statusB))