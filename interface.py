import tkinter as tk
from tkinter import messagebox

import semaforootimizado as so


class Application:
    def __init__(self, master=None):

        vol1, cond1, stt1 = so.val1

        #atribuição do semaforo comum
        statuscA = "Verde"
        statuscB = "Vermelho"

        # dados gerais

        self.SIMSSI = tk.Label(text="SIMSSI")
        self.SIMSSI["font"] = ("Verdana", "10", "bold")

        # titulo sem. otimizado
        self.SemOtm = tk.Label(text="Dados com Semáforo Otimizado")
        self.SemOtm["font"] = ("Verdana", "10", "bold")

        # dados das vias com uso dos semáforos com otimização

        self.SOtxt1 = tk.Label(text="Avenida 1")
        self.SOvol1 = tk.Label(text=" " + vol1)
        self.SOcond1 = tk.Label(text="2")
        self.SOsin1 = tk.Label(text="3")
        self.SObt1 = tk.Button(text="Parada", command=self.botaoA)

        self.SOtxt2 = tk.Label(text="Avenida 2")
        self.SOvol2 = tk.Label(text="1")
        self.SOcond2 = tk.Label(text="2")
        self.SOsin2 = tk.Label(text="3")
        self.SObt2 = tk.Button(text="Parada", command=self.botaoB)

        self.SOtxt3 = tk.Label(text="Avenida 3")
        self.SOvol3 = tk.Label(text="1")
        self.SOcond3 = tk.Label(text="2")
        self.SOsin3 = tk.Label(text="3")
        self.SObt3 = tk.Button(text="Parada", command=self.botaoA)

        self.SOtxt4 = tk.Label(text="Avenida 4")
        self.SOvol4 = tk.Label(text="1")
        self.SOcond4 = tk.Label(text="2")
        self.SOsin4 = tk.Label(text="3")
        self.SObt4 = tk.Button(text="Parada", command=self.botaoB)


        # row 3 - titulo sem. comum
        self.SemCom = tk.Label(text="Dados com Semáforo Comum")
        self.SemCom["font"] = ("Verdana", "10", "bold")

        # row 4 - dados das vias com uso dos semáforos comuns
        self.SCtxt1 = tk.Label(text="Avenida 1")
        self.SCvol1 = tk.Label(text="volume 1")
        self.SCsin1 = tk.Label(text="" + statuscA)

        self.SCtxt2 = tk.Label(text="Avenida 2")
        self.SCvol2 = tk.Label(text="volume 2")
        self.SCsin2 = tk.Label(text="" + statuscB)

        self.SCtxt3 = tk.Label(text="Avenida 3")
        self.SCvol3 = tk.Label(text="volume 3")
        self.SCsin3 = tk.Label(text="" + statuscA)

        self.SCtxt4 = tk.Label(text="Avenida 4")
        self.SCvol4 = tk.Label(text="volume 4")
        self.SCsin4 = tk.Label(text="" + statuscB)

        # row 5 - botões de sair e simulação
        self.sair = tk.Button(text="Sair", width=5, command=self.ExitApp)

        self.simulacao = tk.Button(text="Simulação")

        #criação das grids
        self.SIMSSI.grid(row = 0, column = 0, columnspan= 3, padx = 10, pady = 10)

        self.SemOtm.grid(row = 1, column= 0, columnspan= 3)

        #ruas sinal otm
        self.SOtxt1.grid(row=2, column=0)
        self.SOvol1.grid(row=2, column=1)
        self.SOcond1.grid(row=2, column=2)
        self.SOsin1.grid(row=2, column=3)
        self.SObt1.grid(row=2, column=4)

        self.SOtxt2.grid(row=3, column=0)
        self.SOvol2.grid(row=3, column=1)
        self.SOcond2.grid(row=3, column=2)
        self.SOsin2.grid(row=3, column=3)
        self.SObt2.grid(row=3, column=4)

        self.SOtxt3.grid(row=4, column=0)
        self.SOvol3.grid(row=4, column=1)
        self.SOcond3.grid(row=4, column=2)
        self.SOsin3.grid(row=4, column=3)
        self.SObt3.grid(row=4, column=4)

        self.SOtxt4.grid(row=5, column=0)
        self.SOvol4.grid(row=5, column=1)
        self.SOcond4.grid(row=5, column=2)
        self.SOsin4.grid(row=5, column=3)
        self.SObt4.grid(row=5, column=4)

        self.SemCom.grid(row=6, column=0, columnspan=3)

        #ruas sinais comuns
        self.SCtxt1.grid(row=7, column=0)
        self.SCvol1.grid(row=7, column=1)
        self.SCsin1.grid(row=7, column=3)

        self.SCtxt2.grid(row=8, column=0)
        self.SCvol2.grid(row=8, column=1)
        self.SCsin2.grid(row=8, column=3)

        self.SCtxt3.grid(row=9, column=0)
        self.SCvol3.grid(row=9, column=1)
        self.SCsin3.grid(row=9, column=3)

        self.SCtxt4.grid(row=10, column=0)
        self.SCvol4.grid(row=10, column=1)
        self.SCsin4.grid(row=10, column=3)

        self.sair.grid(row=11, column=1)
        self.simulacao.grid(row=11, column=2)


    def botaoA(self):
        MsgBox = tk.messagebox.askquestion('SIMSSI','Tem certeza que quer acionar a parada dessa via?',icon = 'error')
        if MsgBox == 'yes':
            self.botaoA = "parar"
        return self.botaoA

    def botaoB(self):
        MsgBox = tk.messagebox.askquestion('SIMSSI','Tem certeza que quer acionar a parada dessa via?',icon = 'error')
        if MsgBox == 'yes':
            self.botaoB = "parar"
        return self.botaoB

    def ExitApp(self):
        MsgBox2 = tk.messagebox.askquestion('SIMSSI','Sair do aplicativo?',icon = 'error')
        if MsgBox2 == 'yes':
            root.destroy()




root = tk.Tk()
root.title("SIMSSI - Controle do Administrador")
root.geometry("400x400")

Application(root)

root.mainloop()