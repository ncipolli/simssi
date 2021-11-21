import tkinter as tk
from tkinter import messagebox
import inter

class Application:
    def __init__(self, master=None):

        # dados gerais
        SIMSSI = tk.Label(text="SIMSSI - Controle do Administrador")
        SIMSSI["font"] = ("Verdana", "12", "bold")

        # titulo sem. otimizado
        SemOtm = tk.Label(text="Informações Semafóricas")
        SemOtm["font"] = ("Verdana", "11", "bold")

        # legendas da tabela
        inforua = tk.Label(text="Rua")
        infovol = tk.Label(text="Volume")
        infocond = tk.Label(text="Condição")
        infostt = tk.Label(text="Estágio")
        inforua["font"] = ("Verdana", "10", "bold")
        infovol["font"] = ("Verdana", "10", "bold")
        infocond["font"] = ("Verdana", "10", "bold")
        infostt["font"] = ("Verdana", "10", "bold")

        # dados das vias com uso dos semáforos com otimização

        SOtxt1 = tk.Label(text="RUA A")
        SOvol1 = tk.Label(text="" + inter.vol1)
        SOcond1 = tk.Label(text="" + inter.cond1)
        SOsin1 = tk.Label(text="" + inter.st1)

        SOtxt2 = tk.Label(text="RUA B")
        SOvol2 = tk.Label(text="" + inter.vol2)
        SOcond2 = tk.Label(text="" + inter.cond2)
        SOsin2 = tk.Label(text="" + inter.st2)

        SOtxt3 = tk.Label(text="RUA C")
        SOvol3 = tk.Label(text="" + inter.vol3)
        SOcond3 = tk.Label(text="" + inter.cond3)
        SOsin3 = tk.Label(text="" + inter.st3)

        SOtxt4 = tk.Label(text="RUA D")
        SOvol4 = tk.Label(text="" + inter.vol4)
        SOcond4 = tk.Label(text="" + inter.cond4)
        SOsin4 = tk.Label(text="" + inter.st4)

        # row 3 - titulo informações
        infotxt = tk.Label(text="Informações da Interseção")
        infotxt["font"] = ("Verdana", "11", "bold")

        # row 4 - dados das vias
        txoctxt = tk.Label(text="Taxa de Ocupação:")
        txocval = tk.Label(text="" + inter.toc + "%")

        estxt = tk.Label(text="Estágios")

        vdtxt = tk.Label(text="Tempo de Verde do Ciclo:")
        vdval = tk.Label(text="" + inter.vr + "s")

        amtxt = tk.Label(text="Tempo de Amarelo:")
        amval = tk.Label(text="11 s")

        vmtxt = tk.Label(text="Tempo de Vermelho: ")
        vmval = tk.Label(text="0,19 s")

        # row 5 - botões de sair e simulação
        sair = tk.Button(text="Sair", width=5, command=self.ExitApp)

        #criação das grids
        SIMSSI.grid(row = 0, column = 0, columnspan= 4, padx = 10, pady = 10)

        SemOtm.grid(row = 1, column= 0, columnspan= 4, padx = 10, pady = 10)

        inforua.grid(row=2, column=0, padx=10, pady=10)
        infovol.grid(row=2, column=1, padx=10, pady=10)
        infocond.grid(row=2, column=2, padx=10, pady=10)
        infostt.grid(row=2, column=3, padx=10, pady=10)

        # dados das ruas
        SOtxt1.grid(row=3, column=0, padx=10, pady=10)
        SOvol1.grid(row=3, column=1, padx=10, pady=10)
        SOcond1.grid(row=3, column=2, padx=10, pady=10)
        SOsin1.grid(row=3, column=3, padx=10, pady=10)

        SOtxt2.grid(row=4, column=0, padx=10, pady=10)
        SOvol2.grid(row=4, column=1, padx=10, pady=10)
        SOcond2.grid(row=4, column=2, padx=10, pady=10)
        SOsin2.grid(row=4, column=3, padx=10, pady=10)

        SOtxt3.grid(row=5, column=0, padx=10, pady=10)
        SOvol3.grid(row=5, column=1, padx=10, pady=10)
        SOcond3.grid(row=5, column=2, padx=10, pady=10)
        SOsin3.grid(row=5, column=3, padx=10, pady=10)

        SOtxt4.grid(row=6, column=0, padx=10, pady=10)
        SOvol4.grid(row=6, column=1, padx=10, pady=10)
        SOcond4.grid(row=6, column=2, padx=10, pady=10)
        SOsin4.grid(row=6, column=3, padx=10, pady=10)

        # informações da interseção

        infotxt.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

        txoctxt.grid(row=8, column=0, padx=10, pady=10)
        txocval.grid(row=8, column=1, padx=10, pady=10)

        estxt.grid(row=9, column=0, padx=10, pady=10)
        vdtxt.grid(row=9, column=1, padx=10, pady=10)
        vdval.grid(row=9, column=3, padx=10, pady=10)

        amtxt.grid(row=10, column=1, padx=10, pady=10)
        amval.grid(row=10, column=3, padx=10, pady=10)

        vmtxt.grid(row=11, column=1, padx=10, pady=10)
        vmval.grid(row=11, column=3, padx=10, pady=10)

        # botão sair

        sair.grid(row=12, column=0, columnspan=4, padx=10, pady=10)

    def ExitApp(self):
        MsgBox2 = tk.messagebox.askquestion('SIMSSI','Sair do aplicativo?',icon = 'error')
        if MsgBox2 == 'yes':
            root.destroy()

root = tk.Tk()
Application(root)
root.title("SIMSSI - Simulação da Implementação de Sistema Semafórico em Tempo Real")
root.resizable(False, False)
window_height = 600
window_width = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.mainloop()