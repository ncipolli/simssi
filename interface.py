from tkinter import *

import codigo

class Application:
    def __init__(self, master=None):

        # dados gerais

        self.SIMSSI = Label(text="SIMSSI")
        self.SIMSSI["font"] = ("Verdana", "10", "bold")

        # titulo sem. otimizado
        self.SemOtm = Label(text="Dados com Semáforo Otimizado")
        self.SemOtm["font"] = ("Verdana", "10", "bold")

        # dados das vias com uso dos semáforos com otimização

        self.SOtxt1 = Label(text="Avenida 1")
        self.SOvol1 = Label(text="" + str(codigo.val1[0]))
        self.SOcond1 = Label(text="" + str(codigo.val1[1]))
        self.SOsin1 = Label(text="" + str(codigo.val1[2]))
        self.SObt1 = Button(text="Parada", command=self.mudarTexto)

        self.SOtxt2 = Label(text="Avenida 2")
        self.SOvol2 = Label(text="" + str(codigo.val2[0]))
        self.SOcond2 = Label(text="" + str(codigo.val2[1]))
        self.SOsin2 = Label(text="" + str(codigo.val2[2]))
        self.SObt2 = Button(text="Parada", command=self.mudarTexto)

        self.SOtxt3 = Label(text="Avenida 3")
        self.SOvol3 = Label(text="" + str(codigo.val3[0]))
        self.SOcond3 = Label(text="" + str(codigo.val3[1]))
        self.SOsin3 = Label(text="" + str(codigo.val3[2]))
        self.SObt3 = Button(text="Parada", command=self.mudarTexto)

        self.SOtxt4 = Label(text="Avenida 4")
        self.SOvol4 = Label(text="" + str(codigo.val4[0]))
        self.SOcond4 = Label(text="" + str(codigo.val4[1]))
        self.SOsin4 = Label(text="" + str(codigo.val4[2]))
        self.SObt4 = Button(text="Parada", command=self.mudarTexto)


        # row 3 - titulo sem. comum
        self.SemCom = Label(text="Dados com Semáforo Comum")
        self.SemCom["font"] = ("Verdana", "10", "bold")

        # row 4 - dados das vias com uso dos semáforos comuns
        self.SCtxt1 = Label(text="Avenida 1")
        self.SCvol1 = Label(text="volume 1")
        self.SCsin1 = Label(text="sinal 1")

        self.SCtxt2 = Label(text="Avenida 2")
        self.SCvol2 = Label(text="volume 2")
        self.SCsin2 = Label(text="sinal2")

        self.SCtxt3 = Label(text="Avenida 3")
        self.SCvol3 = Label(text="volume 3")
        self.SCsin3 = Label(text="sinal 3")

        self.SCtxt4 = Label(text="Avenida 4")
        self.SCvol4 = Label(text="volume 4")
        self.SCsin4 = Label(text="sinal 4")

        # row 5 - botões de sair e simulação
        self.sair = Button(text="Sair", width=5)

        self.simulacao = Button(text="Simulação")

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



    def mudarTexto(self):
        if self.SOtxt1["text"] == "Atualizado":
            self.SOtxt1["text"] = "Aguardando atualização"
        else:
            self.SOtxt1["text"] = "Atualizado"




root = Tk()
root.title("SIMSSI - Controle do Usuário")
root.geometry("400x400")

Application(root)
root.mainloop()