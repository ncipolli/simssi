from tkinter import *

import codigo

class Application:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["padx"] = 0
        self.container1["pady"] = 5
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 0
        self.container2["pady"] = 20
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 0
        self.container3["pady"] = 30
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 0
        self.container4["pady"] = 40
        self.container4.pack()

        # container 1 - dados gerais

        self.Titulo = Label(self.container1, text="SIMSSI")
        self.Titulo["font"] = ("Verdana", "10", "bold")
        self.Titulo.pack()

        # container 2 - dados das vias com uso dos semáforos com otimização

        self.Titulo1 = Label(self.container2, text="Dados com Semáforo Otimizado")
        self.Titulo1["font"] = ("Verdana", "10", "bold")
        self.Titulo1.pack()

        self.txt = Label(self.container2, text="Para emergências, aperte o botão")
        self.txt.pack()

        self.bt = Button(self.container2)
        self.bt["text"] = "Parada"
        self.bt["width"] = 5
        self.bt["command"] = self.mudarTexto
        self.bt.pack(side=LEFT)

        # container 3 - dados das vias com uso dos semáforos sem otimização

        self.Titulo2 = Label(self.container3, text="Dados com Semáforo Comum")
        self.Titulo2["font"] = ("Verdana", "10", "bold")
        self.Titulo2.pack()

        # container 4 - dados finais
        self.txt4 = Label(self.container4, text="creditos")
        self.txt4.pack()

        self.sair = Button(self.container4)
        self.sair["text"] = "Sair"
        self.sair["width"] = 5
        self.sair["command"] = self.container4.quit
        self.sair.pack(side=LEFT)

    def mudarTexto(self):
        if self.txt["text"] == "Para emergências, aperte o botão":
            self.txt["text"] = "Aguardando atualização"
        else:
            self.txt["text"] = "Para emergências, aperte o botão"




root = Tk()
root.title("SIMSSI - Controle do Usuário")
root.geometry("500x500")

Application(root)
root.mainloop()