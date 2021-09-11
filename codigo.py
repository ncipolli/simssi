# intersessão em X

# !! - a fazer
# !!!! - corrigir

import time, random

class SinalOtimizado:
    def __init__(self):        
        pass

    def gerarDados(self, volumeAnt):

        if volumeAnt == 0:
            volume = random.sample(range(1, 50), 4)
        else:
            for index, value in enumerate(volumeAnt):
                if value < 0:
                    volumeAnt[index] = 0

            #print("primeiro def")
            #print(self.volumeAnt)


            self.volumeProx = random.sample(range(1, 10), 4)
            volume = [val1 + val2 for val1, val2 in zip(volumeAnt, self.volumeProx)]

        condicao = random.choices(["pedestre", "viatura", "emergencia", "nenhum"], [2, 1, 1, 6], k=4)

        return volume, condicao

    # tempo real
    def calculoCiclo(self, volume, condicao):
        # tempo perdido (s)
        # !!!!
        if condicao[0] == "pedestre" or condicao[1] == "pedestre" or condicao[2] == "pedestre" or condicao[3] == "pedestre":
            self.tp = 28
        else:
            self.tp = 18

        # taxa de ocupação (ucp/h)
        self.y = sum(volume) / 1800

        # tempo de ciclo ótimo (s)
        self.tco = ((1.5 * 28) + 5) / (1 - (self.y * 1 + self.y * 2))

        # !! O tempo de ciclo deve ser ajustado para um múltiplo de 5 s (para C < 90 s) ou 10 s (para C > 90 S).
        # !! Todos os intervalos devem ser arredondados para serem múltiplos de um segundo.
        self.tc = round(self.tco)

        return self.tc


    def definicaoCiclo(self, volume):

        self.statusA = "verde"
        self.statusB = "vermelho"

        # !!!! troca de status

        # !! if condição
        '''if stop == True
            status = vermelho
        else
            codigo'''

        # volume anterior

        self.val = random.sample(range(5, 10), 2)

        # !!!! não deixar ir negativo
        if self.statusA == "verde":
            self.retirada = [self.val[0], 0, self.val[1], 0]
            self.volumeAnt = [valA - valB for valA, valB in zip(volume, self.retirada)]
        else:
            self.retirada = [0, self.val[0], 0, self.val[1]]
            self.volumeAnt = [valA - valB for valA, valB in zip(volume, self.retirada)]

        self.status = [self.statusA, self.statusB]

        #print(self.volumeAnt)
        return self.volumeAnt, self.status
    

# atribuição de valores
# isso pode ser gerado diretamente na interface
    def atribuicaoValores(self, volume, condicao, status):

        statusA, statusB = status

        self.av_um = [volume[0], condicao[0],  statusA]
        self.av_dois = [volume[1], condicao[1], statusB]
        self.av_tres = [volume[2], condicao[2], statusA]
        self.av_quatro = [volume[3], condicao[3], statusB]

        #print("avs: ")
        #print(self.av_um, self.av_dois, self.av_tres, self.av_quatro)

        return self.av_um, self.av_dois, self.av_tres, self.av_quatro


# função do semáforo comum
    def semaforoComum(self):

        # valor de tempo de ciclo pré determinado
        self.tc = 10

        # troca de status
        self.statusA = "vermelho"
        self.statusB = "vermelho"
        print(self.statusA, self.statusB)
        time.sleep(2)

        self.statusA = "verde"
        self.val = random.sample(range(5, 10), 2)
        self.retirada = [self.val[0], 0, self.val[1], 0]
        self.volumeAnt = [valA - valB for valA, valB in zip(volume, self.retirada)]
        print(self.statusA, self.statusB, self.volumeAnt)
        time.sleep(self.tc)

        self.statusA = "amarelo"
        print(self.statusA, self.statusB)
        time.sleep(2)

        self.statusA = "vermelho"
        print(self.statusA, self.statusB)
        time.sleep(2)

        self.statusB = "verde"
        self.val = random.sample(range(5, 10), 2)
        self.retirada = [0, self.val[0], 0, self.val[1]]
        self.volumeAnt = [valA - valB for valA, valB in zip(volume, self.retirada)]
        print(self.statusA, self.statusB, self.volumeAnt)
        time.sleep(self.tc)

        self.statusB = "amarelo"
        print(self.statusA, self.statusB)
        time.sleep(2)

        self.statusc = [self.statusA, self.statusB]

        if volumeAnt == 0:
            self.volume = random.sample(range(1, 50), 4)

        else:
            self.volumeProx = random.sample(range(1, 10), 4)
            self.volume = [val1 + val2 for val1, val2 in zip(volumeAnt, self.volumeProx)]

        print(self.volumeAnt, self.volumeProx, self.volume)
        return self.statusc, self.volume
        

sinalOtimizado = SinalOtimizado()

volumeAnt = 0

#if __name__ == '__main__':
    #print(sinalOtimizado.atribuicaoValores(volume, condicao, statusA, statusB))

while True:
    volume, condicao = sinalOtimizado.gerarDados(volumeAnt)
    tco = sinalOtimizado.calculoCiclo(volume, condicao)
    volumeAnt, status = sinalOtimizado.definicaoCiclo(volume)
    val1, val2, val3, val4 = sinalOtimizado.atribuicaoValores(volume, condicao, status)
    
    time.sleep(20)

