# intersessão em X

# !! - a fazer
# !!!! - corrigir

import schedule
import time
import random

class SinalOtimizado:
    def __init__(self):        
        pass

#recebe volumeAnt
    def gerarDados(self, volumeAnt):

        if volumeAnt == 0:
            volume = random.sample(range(1, 50), 4)
            print("volumeAnt = 0")

        else:
            self.volumeProx = random.sample(range(1, 10), 4)
            volume = [val1 + val2 for val1, val2 in zip(volumeAnt, self.volumeProx)]
            print("volumeAnt =/ 0")

        condicao = random.choices(["pedestre", "viatura", "emergencia", "nenhum"], [2, 1, 1, 6], k=4)

        print(volume, condicao)

        return volume, condicao

    #!! tempo fixo

    # tempo real
    def calculoCiclo(self, volume, condicao):
        # tempo perdido (s)
        # !!!!
        if condicao == "pedestre":
            self.tp = 28
            print("pedestre = true")
        else:
            self.tp = 18
            print("pedestre = false")

        # taxa de ocupação (ucp/h)
        self.y = sum(volume) / 1800

        # tempo de ciclo ótimo (s)
        self.tco = ((1.5 * 28) + 5) / (1 - (self.y * 1 + self.y * 2))

        # !! O tempo de ciclo deve ser ajustado para um múltiplo de 5 s (para C < 90 s) ou 10 s (para C > 90 S).
        # !! Todos os intervalos devem ser arredondados para serem múltiplos de um segundo.
        self.tc = round(self.tco)

        print(self.tc)
        return self.tc


    def definicaoCiclo(self, volume):

        self.statusA = "verde"
        self.statusB = "vermelho"

        # !!!! troca de status
        self.statusA = self.statusB
        self.statusB = self.statusA

        # !! if condição

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

        print(self.volumeAnt, self.status)
        return self.volumeAnt, self.status
    

# atribuição de valores
# isso pode ser gerado diretamente na interface
    def atribuicaoValores(self, volume, condicao, status):

        statusA, statusB = status

        self.av_um = [volume[0], condicao[0],  statusA]
        self.av_dois = [volume[1], condicao[1], statusB]
        self.av_tres = [volume[2], condicao[2], statusA]
        self.av_quatro = [volume[3], condicao[3], statusB]

        print(self.av_um, self.av_dois, self.av_tres, self.av_quatro)

        return self.av_um, self.av_dois, self.av_tres, self.av_quatro
        

sinalOtimizado = SinalOtimizado()
volumeAnt = 0
volume, condicao = sinalOtimizado.gerarDados(volumeAnt)
tco = sinalOtimizado.calculoCiclo(volume, condicao)
volumeAnt, status = sinalOtimizado.definicaoCiclo(volume)
val1, val2, val3, val4 = sinalOtimizado.atribuicaoValores(volume, condicao, status)

#val1, val2, val3, val4 = sinalOtimizado.atribuicaoValores(volume, condicao, statusA, statusB)

#if __name__ == '__main__':
    #print(sinalOtimizado.atribuicaoValores(volume, condicao, statusA, statusB))

#schedule.every(20).seconds.do(sinalOtimizado.calculoCiclo)

#while True:
 #   schedule.run_pending()
  #  time.sleep(5)

