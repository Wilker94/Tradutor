import tkinter as tk
#from atualizador import set_window_position
from interface import *


inicial = tk.Tk()
inicial.title("Tradutor de Texto")
#set_window_position(inicial)


screen_width = inicial.winfo_screenwidth()
screen_height = inicial.winfo_screenheight()

window_width = 1100  # Largura da janela
window_height = 800  # Altura da janela

# Calculando a posição para centralizar a janela
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)


inicial.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


telas(inicial)
inicial.mainloop()


#proxsteps
#pasta nome arquivo
#copiar embaixo de texto
#ctrl z, tab
#config:
# voz (pessoa de voz, similaridade)
#adicionar opcional +1 em final nome caso exista ou substituir
#Adicionar diretorio em config


#WK 797ccf834e6e157ff1354554b2e93f12
#Wonka1 be00df312290494f3d432b0af6f9bc6c
#NSEW = CIMA BAIXO DIREITA ESQUERDA
#Y= CIMA/BAIXO
#X= DIREITA ESQUERDA

#pip install pyinstaller
#pyinstaller --onefile main.py



















