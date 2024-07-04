import tkinter as tk
from tkinter import scrolledtext

def telas(tela):
    
    def mudar_texto():
        texto = texto_traducao_input.get("1.0", tk.END).strip()  # Obtém o texto digitado na ScrolledText
        
        # Atualiza as labels de acordo com o texto
        translate_portugues_label.config(text="Português")
        translate_portugues_text.config(text=texto)
        checkbox_portugues.grid(row=6, column=0, padx=(10,0), pady=0, sticky=tk.W if translate_portugues.get() else tk.N)
        
        translate_ingles_label.config(text="Inglês")
        translate_ingles_text.config(text=texto)
        checkbox_ingles.grid(row=6, column=1, padx=(10,0), pady=0, sticky=tk.W if translate_ingles.get() else tk.N)

        translate_espanhol_label.config(text="Espanhol")
        translate_espanhol_text.config(text=texto)
        checkbox_espanhol.grid(row=6, column=2, padx=(10,0), pady=0, sticky=tk.W if translate_espanhol.get() else tk.N)

        translate_frances_label.config(text="Francês")
        translate_frances_text.config(text=texto)
        checkbox_frances.grid(row=6, column=3, padx=(10,0), pady=0, sticky=tk.W if translate_frances.get() else tk.N)

        translate_alemao_label.config(text="Alemão")
        translate_alemao_text.config(text=texto)
        checkbox_alemao.grid(row=6, column=4, padx=(10,0), pady=0, sticky=tk.W if translate_alemao.get() else tk.N)

        translate_italiano_label.config(text="Italiano")
        translate_italiano_text.config(text=texto)
        checkbox_italiano.grid(row=6, column=5, padx=(10,0), pady=0, sticky=tk.W if translate_italiano.get() else tk.N)
    
    def checkbox_selecionada(*args):
        mudar_texto()  # Chama mudar_texto() sempre que uma checkbox é selecionada
        
    # Criar a janela principal
    tela.title("Tradução de Texto")
    
    # Campo de solicitação de texto
    texto_traducao_input = scrolledtext.ScrolledText(tela, width=62, height=2)
    texto_traducao_input.grid(row=4, column=0, columnspan=5, padx=(10,0), pady=(0,10), sticky=tk.W)
    
    # Labels e Checkbuttons para idiomas
    translate_portugues = tk.BooleanVar(tela)
    translate_portugues.trace_add("write", checkbox_selecionada)
    checkbox_portugues = tk.Checkbutton(tela, variable=translate_portugues)
    checkbox_portugues.grid(row=6, column=0, padx=(10,0), pady=0, sticky=tk.N)
    translate_portugues_label = tk.Label(tela, text="")
    translate_portugues_label.grid(row=6, column=0, padx=(30,60), pady=2, sticky=tk.W)
    translate_portugues_text = tk.Label(tela, text="", wraplength=120)
    translate_portugues_text.grid(row=7, column=0, padx=(10,0), pady=2, sticky=tk.W)

    translate_ingles = tk.BooleanVar(tela)
    translate_ingles.trace_add("write", checkbox_selecionada)
    checkbox_ingles = tk.Checkbutton(tela, variable=translate_ingles)
    checkbox_ingles.grid(row=6, column=1, padx=(10,0), pady=0, sticky=tk.N)
    translate_ingles_label = tk.Label(tela, text="")
    translate_ingles_label.grid(row=6, column=1, padx=(30,60), pady=2, sticky=tk.W)
    translate_ingles_text = tk.Label(tela, text="", wraplength=120)
    translate_ingles_text.grid(row=7, column=1, padx=(10,0), pady=2, sticky=tk.W)

    translate_espanhol = tk.BooleanVar(tela)
    translate_espanhol.trace_add("write", checkbox_selecionada)
    checkbox_espanhol = tk.Checkbutton(tela, variable=translate_espanhol)
    checkbox_espanhol.grid(row=6, column=2, padx=(10,0), pady=0, sticky=tk.N)
    translate_espanhol_label = tk.Label(tela, text="")
    translate_espanhol_label.grid(row=6, column=2, padx=(30,60), pady=2, sticky=tk.W)
    translate_espanhol_text = tk.Label(tela, text="", wraplength=120)
    translate_espanhol_text.grid(row=7, column=2, padx=(10,0), pady=2, sticky=tk.W)

    translate_frances = tk.BooleanVar(tela)
    translate_frances.trace_add("write", checkbox_selecionada)
    checkbox_frances = tk.Checkbutton(tela, variable=translate_frances)
    checkbox_frances.grid(row=6, column=3, padx=(10,0), pady=0, sticky=tk.N)
    translate_frances_label = tk.Label(tela, text="")
    translate_frances_label.grid(row=6, column=3, padx=(30,60), pady=2, sticky=tk.W)
    translate_frances_text = tk.Label(tela, text="", wraplength=120)
    translate_frances_text.grid(row=7, column=3, padx=(10,0), pady=2, sticky=tk.W)

    translate_alemao = tk.BooleanVar(tela)
    translate_alemao.trace_add("write", checkbox_selecionada)
    checkbox_alemao = tk.Checkbutton(tela, variable=translate_alemao)
    checkbox_alemao.grid(row=6, column=4, padx=(10,0), pady=0, sticky=tk.N)
    translate_alemao_label = tk.Label(tela, text="")
    translate_alemao_label.grid(row=6, column=4, padx=(30,60), pady=2, sticky=tk.W)
    translate_alemao_text = tk.Label(tela, text="", wraplength=120)
    translate_alemao_text.grid(row=7, column=4, padx=(10,0), pady=2, sticky=tk.W)

    translate_italiano = tk.BooleanVar(tela)
    translate_italiano.trace_add("write", checkbox_selecionada)
    checkbox_italiano = tk.Checkbutton(tela, variable=translate_italiano)
    checkbox_italiano.grid(row=6, column=5, padx=(10,0), pady=0, sticky=tk.N)
    translate_italiano_label = tk.Label(tela, text="")
    translate_italiano_label.grid(row=6, column=5, padx=(30,60), pady=2, sticky=tk.W)
    translate_italiano_text = tk.Label(tela, text="", wraplength=120)
    translate_italiano_text.grid(row=7, column=5, padx=(10,0), pady=2, sticky=tk.W)

    # Mostra a interface
    tela.mainloop()

# Executa a função para criar a interface
telas(tk.Tk())
