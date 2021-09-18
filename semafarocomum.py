import random, time

class SemaforoComum:
    def __init__(self) -> None:
        #no need for this sh*t
        pass

    def semaforo_comum(self):
        volume = random.sample(range(1, 50), 4)
        
        tc=10

        statusA = "vermelho"
        statusB = "vermelho"
        print(statusA, statusB)
        time.sleep(2)

        statusA = "verde"
        val = random.sample(range(5, 10), 2)
        retirada = [val[0], 0, val[1], 0]
        volumeAnt = [valA - valB for valA, valB in zip(volume, retirada)]

        for index, value in enumerate(volumeAnt):
                if value < 0:
                    volumeAnt[index] = 0

        print(statusA, statusB)
        time.sleep(tc)

        statusA = "amarelo"
        print(statusA, statusB)
        time.sleep(2)

        statusA = "vermelho"
        print(statusA, statusB)
        time.sleep(2)

        statusB = "verde"
        val = random.sample(range(5, 10), 2)
        retirada = [0, val[0], 0, val[1]]
        volumeAnt = [valA - valB for valA, valB in zip(volume, retirada)]

        for index, value in enumerate(volumeAnt):
                if value < 0:
                    volumeAnt[index] = 0

        print(statusA, statusB)
        time.sleep(tc)

        status = [statusA, statusB]

        if volumeAnt == 0:
            volume = random.sample(range(1, 50), 4)
        else:
            volumeProx = random.sample(range(1, 10), 4)
            volume = [val1 + val2 for val1, val2 in zip(volumeAnt, volumeProx)]

        print(status, volume)

        return status



sc = SemaforoComum()
volumeAnt = 0

while True:
    sc.semaforo_comum()
    time.sleep(1)