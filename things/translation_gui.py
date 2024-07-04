import tkinter as tk
from tkinter import scrolledtext, messagebox, IntVar
#from translate import translate_text
from things.character_counter import CharacterCounter
from translate import tradutor

class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tradutor de Texto")
        self.root.geometry("800x600")
        
        
        
        #contador de caracteres
        self.char_counter = CharacterCounter(self.root)
        self.char_counter.grid(row=0, column=0, columnspan=8, padx=10, pady=10, sticky=tk.NE)  # Posicionar no topo direito

        # Campo de entrada para a API elevenlabs
        self.api_label = tk.Label(self.root, text="Digite a API do Elevenlabs:")
        self.api_label.grid(row=1, column=0, columnspan=8, padx=10, pady=(10, 0), sticky=tk.W)

        self.api_input = scrolledtext.ScrolledText(self.root, width=32, height=2, wrap=tk.WORD)
        self.api_input.grid(row=2, column=0, columnspan=8, padx=10, pady=(0, 10), sticky=tk.W)

        # Campo de entrada para o texto a ser traduzido
        texto_user = tk.Label(self.root, text="Digite o texto que deseja traduzir:")
        texto_user.grid(row=3, column=0, columnspan=8, padx=10, pady=(10, 0), sticky=tk.W)

        self.text_input = scrolledtext.ScrolledText(self.root, width=60, height=5, wrap=tk.WORD)
        self.text_input.grid(row=4, column=0, columnspan=8, padx=10, pady=(0, 10), sticky=tk.W)

        # Botão para traduzir o texto
        self.translate_button = tk.Button(self.root, text="Traduzir", command=tradutor)
        self.translate_button.grid(row=5, column=0, padx=10, pady=(10, 0), sticky=tk.W)

    """def translate_text(self):
        # Limpar textos antigos
        self.clear_translations()

        # Obter o texto digitado pelo usuário para traduzir
        original_text = self.text_input.get("1.0", tk.END).strip()

        # Verificar se o texto original está vazio
        if not original_text:
            messagebox.showwarning("Aviso", "Por favor, digite um texto para traduzir.")
            return

        try:
            # Obter a chave de API do Elevenlabs
            api_key = self.api_input.get("1.0", tk.END).strip()
            # Aqui você pode inserir a lógica para utilizar a API ou serviço de tradução desejado

            # Exibir texto traduzido para Alemão, Inglês e Espanhol
            translations = translate_text(original_text)
            translated_german = translations['de']
            translated_english = translations['en']
            translated_spanish = translations['es']

            # Exibir texto traduzido para Alemão
            self.translate_to_german_var = tk.BooleanVar()
            self.translate_to_german_checkbox = tk.Checkbutton(self.root, variable=self.translate_to_german_var)
            self.translate_to_german_checkbox.grid(row=6, column=1, padx=10, pady=(10, 0), sticky=tk.W)
            self.translated_german_label = tk.Label(self.root, text="Alemão:", wraplength=280)
            self.translated_german_label.grid(row=6, column=0, padx=10, pady=(10, 0), sticky=tk.W)
            self.translated_german_text = tk.Label(self.root, text=translated_german, wraplength=280)
            self.translated_german_text.grid(row=7, column=0, padx=10, pady=(0, 10), sticky=tk.W)

            # Exibir texto traduzido para Inglês
            self.translate_to_english_var = tk.BooleanVar()
            self.translate_to_english_checkbox = tk.Checkbutton(self.root, variable=self.translate_to_english_var)
            self.translate_to_english_checkbox.grid(row=8, column=1, padx=10, pady=(10, 0), sticky=tk.W)
            self.translated_english_label = tk.Label(self.root, text="Inglês:", wraplength=280)
            self.translated_english_label.grid(row=8, column=0, padx=10, pady=(10, 0), sticky=tk.W)
            self.translated_english_text = tk.Label(self.root, text=translated_english, wraplength=280)
            self.translated_english_text.grid(row=9, column=0, padx=10, pady=(0, 10), sticky=tk.W)

            # Exibir texto traduzido para Espanhol
            self.translate_to_spanish_var = tk.BooleanVar()
            self.translate_to_spanish_checkbox = tk.Checkbutton(self.root, variable=self.translate_to_spanish_var)
            self.translate_to_spanish_checkbox.grid(row=10, column=1, padx=10, pady=(10, 0), sticky=tk.W)
            self.translated_spanish_label = tk.Label(self.root, text="Espanhol:", wraplength=280)
            self.translated_spanish_label.grid(row=10, column=0, padx=10, pady=(10, 0), sticky=tk.W)
            self.translated_spanish_text = tk.Label(self.root, text=translated_spanish, wraplength=280)
            self.translated_spanish_text.grid(row=11, column=0, padx=10, pady=(0, 10), sticky=tk.W)

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao traduzir o texto:\n{str(e)}")

    def clear_translations(self):
        # Limpar textos traduzidos antigos, se existirem
        if hasattr(self, 'translated_german_label'):
            self.translated_german_label.destroy()
        if hasattr(self, 'translated_german_text'):
            self.translated_german_text.destroy()
        if hasattr(self, 'translated_english_label'):
            self.translated_english_label.destroy()
        if hasattr(self, 'translated_english_text'):
            self.translated_english_text.destroy()
        if hasattr(self, 'translated_spanish_label'):
            self.translated_spanish_label.destroy()
        if hasattr(self, 'translated_spanish_text'):
            self.translated_spanish_text.destroy()


    def run(self):
        self.root.mainloop()"""

# Executar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    app.run()
