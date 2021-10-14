# interseção 4 vias

import time, random

class SinalOtimizado:
    def __init__(self):
        #    
        pass

    def gerar_dados(self, volumeAnt):
        if volumeAnt == 0:
            volume = random.sample(range(1, 50), 4)
        else:
            for index, value in enumerate(volumeAnt):
                if value < 0:
                    volumeAnt[index] = 0

            volumeProx = random.sample(range(1, 10), 4)
            volume = [val1 + val2 for val1, val2 in zip(volumeAnt, volumeProx)]

        condicao = random.choices(["pedestre", "viatura", "emergencia", "nenhum"], [2, 1, 1, 6], k=4)

        return volume, condicao


    def calculo_ciclo(self, volume, condicao):
        # tempo perdido (s)
        if "pedestre" in condicao:
            tp = 22.9
        else:
            tp = 12

        # tempo de vermelho geral (s)
        #tvg = 0.31

        # taxa de ocupação (ucp/h)
        #ton = taxa de ocupação do estagio n
        to1 = (volume[0] + volume[2]) / 2000
        to2 = (volume[1] + volume[3]) / 2000
        tot = sum(volume) / 2000

        # tempo de ciclo ótimo (s)
        tco = (1.5 * tp + 5) / (1 - tot)
        
        tc = round(tco)

        # tempo de verde efetivo (s)
        tve1 = (tco  - tp) * (to1 / tot)
        tve2 = (tco  - tp) * (to2 / tot)
        tve = tve1 + tve2

        # tempo de verde real (s)
        #tvr = tve - tvg + tp

        return tc, tve, tot


    def definicao_status(self, volume, condicao):
        statusA = "vermelho"
        statusB = "vermelho"

        # considerar botões

        if condicao[0] == "emergencia" or condicao[2] == "emergencia":
            statusA = "verde"
            statusB = "vermelho"
        elif condicao[1] == "emergencia" or condicao[3] == "emergencia":
            statusA = "vermelho"
            statusB = "verde"
        else:
            volumeA = volume[0] + volume[2]
            volumeB = volume [1] + volume[3]
            if  volumeA > volumeB:
                statusA = "verde"
                statusB = "vermelho"
            elif volumeB > volumeA:
                statusA = "vermelho"
                statusB = "verde"

        status = [statusA, statusB]

        return status
    

    def volume_anterior(self, status):
        val = random.sample(range(10, 20), 2)

        if status[0] == "verde":
            retirada = [val[0], 0, val[1], 0]
            volumeAnt = [valA - valB for valA, valB in zip(volume, retirada)]
        else:
            retirada = [0, val[0], 0, val[1]]
            volumeAnt = [valA - valB for valA, valB in zip(volume, retirada)]

        return volumeAnt


    def atribuicao_valores(self, volume, condicao, status):

        statusA, statusB = status

        av_um = [volume[0], condicao[0],  statusA]
        av_dois = [volume[1], condicao[1], statusB]
        av_tres = [volume[2], condicao[2], statusA]
        av_quatro = [volume[3], condicao[3], statusB]

        return av_um, av_dois, av_tres, av_quatro
        

so = SinalOtimizado()

volumeAnt = 0

#if __name__ == '__main__':
    #print(so.atribuicaoValores(volume, condicao, statusA, statusB))

while True:
    volume, condicao = so.gerar_dados(volumeAnt)
    tc, tve, tot = so.calculo_ciclo(volume, condicao)
    status = so.definicao_status(volume, condicao)
    volumeAnt = so.volume_anterior(status)
    val1, val2, val3, val4 = so.atribuicao_valores(volume, condicao, status)

    print("dados:")
    print(volume, condicao, tc, tve, tot, status)
    
    time.sleep(tc)
