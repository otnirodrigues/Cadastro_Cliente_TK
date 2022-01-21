
from tkinter import *
from turtle import title

# criando o modelo tk
root = Tk()

class Application():

    # criando um metodo de inicialização, onde instancia a variavel global root
    # Chama o metodo tela(), que contem as configurações da janela
    # Inicia o loop da janela do TK

    def __init__(self):
       self.root = root
       self.tela()
       root.mainloop()

    def tela(self):
        
        # Configurando o titulo da janela
        self.root.title('Cadastro de Clientes')      

        #configurando a cor de fundo da tela
        self.root.configure(background='#008080')

        # Configurando o tamanho de inicio da janela
        self.root.geometry('600x400')

        # Configurando a tela para ser responssiva na vertical e horizontal
        self.root.resizable(True, True)

        # Configurando a janela alcançar um tamanho maximo e minimo
        self.root.wm_minsize(200 , 200)
        self.root.wm_maxsize(800 , 700)

Application()
