# intersessão em X

# !! - a fazer
# !!!! - corrigir

import time, random, csv

class SinalOtimizado:
    def __init__(self):
        #no need for this sh*t        
        pass

    def gerar_dados(self, volumeAnt):

        if volumeAnt == 0:
            volume = random.sample(range(1, 50), 4)
        else:
            for index, value in enumerate(volumeAnt):
                if value < 0:
                    volumeAnt[index] = 0

            self.volumeProx = random.sample(range(1, 10), 4)
            volume = [val1 + val2 for val1, val2 in zip(volumeAnt, self.volumeProx)]

        condicao = random.choices(["pedestre", "viatura", "emergencia", "nenhum"], [2, 1, 1, 6], k=4)

        return volume, condicao


    def calculo_ciclo(self, volume, condicao):
        # tempo perdido (s)
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


    def definicao_ciclo(self, volume, condicao):

        self.statusA = "amarelo"
        self.statusB = "amarelo"

        # troca de status
        # considerar botões

        if condicao[0] == "emergencia" or condicao[2] == "emergencia":
            self.statusA = "verde"
            self.statusB = "vermelho"
        elif condicao[1] == "emergencia" or condicao[3] == "emergencia":
            self.statusA = "vermelho"
            self.statusB = "verde"
        else:
            volumeA = volume[0] + volume[2]
            volumeB = volume [1] + volume[3]
            if  volumeA > volumeB:
                self.statusA = "verde"
                self.statusB = "vermelho"
            elif volumeB > volumeA:
                self.statusA = "vermelho"
                self.statusB = "verde"

        self.status = [self.statusA, self.statusB]

        return self.status
    

    def volume_anterior(self, status):
        self.val = random.sample(range(5, 10), 2)

        if self.status[0] == "verde":
            self.retirada = [self.val[0], 0, self.val[1], 0]
            self.volumeAnt = [valA - valB for valA, valB in zip(volume, self.retirada)]
        else:
            self.retirada = [0, self.val[0], 0, self.val[1]]
            self.volumeAnt = [valA - valB for valA, valB in zip(volume, self.retirada)]

        return self.volumeAnt


    def atribuicao_valores(self, volume, condicao, status):

        statusA, statusB = status

        self.av_um = [volume[0], condicao[0],  statusA]
        self.av_dois = [volume[1], condicao[1], statusB]
        self.av_tres = [volume[2], condicao[2], statusA]
        self.av_quatro = [volume[3], condicao[3], statusB]

        return self.av_um, self.av_dois, self.av_tres, self.av_quatro
        

so = SinalOtimizado()

volumeAnt = 0

#if __name__ == '__main__':
    #print(so.atribuicaoValores(volume, condicao, statusA, statusB))

while True:
    volume, condicao = so.gerar_dados(volumeAnt)
    tco = so.calculo_ciclo(volume, condicao)
    status = so.definicao_ciclo(volume, condicao)
    volumeAnt = so.volume_anterior(status)
    val1, val2, val3, val4 = so.atribuicao_valores(volume, condicao, status)
    
    #print(volume, condicao, tco, status)
    
    #ele só roda depois da mudança de status
    time.sleep(tco)
