from deep_translator import GoogleTranslator
import tkinter as tk

 
def translate_text(text, language):
    translator = GoogleTranslator(source='auto', target=language)
    translation = translator.translate(text)
    return translation


def traduz_texto(texto_traducao_input, checkbox_portugues, translate_portugues_label, translate_portugues_text, 
        checkbox_ingles, translate_ingles_label, translate_ingles_text, checkbox_espanhol, translate_espanhol_label, translate_espanhol_text, 
        checkbox_frances, translate_frances_label, translate_frances_text, checkbox_alemao, translate_alemao_label, translate_alemao_text,
        checkbox_italiano, translate_italiano_label, translate_italiano_text):
       
        
    textos = texto_traducao_input.get("1.0", tk.END)  # Obtém o texto digitado na ScrolledText       
    
    translate_portugues_label.config(text="Português")
    checkbox_portugues.grid(row=6, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translate_portugues_text.config(text=textos)
               
    translate_ingles_label.config(text="Inglês")
    checkbox_ingles.grid(row=6, column=1, padx=(10,0), pady=0, sticky=tk.W)
    traducao_ingles = translate_text(textos, 'en')
    translate_ingles_text.config(text=traducao_ingles)
               
    translate_espanhol_label.config(text="Espanhol")
    checkbox_espanhol.grid(row=6, column=2, padx=(10,0), pady=0, sticky=tk.W)
    traducao_espanhol = translate_text(textos, 'es')
    translate_espanhol_text.config(text=traducao_espanhol)
        
    translate_frances_label.config(text="Francês")
    checkbox_frances.grid(row=6, column=3, padx=(10,0), pady=0, sticky=tk.W)
    traducao_frances = translate_text(textos, 'fr')
    translate_frances_text.config(text=traducao_frances)
        
    translate_alemao_label.config(text="Alemão")
    checkbox_alemao.grid(row=6, column=4, padx=(10,0), pady=0, sticky=tk.W)
    traducao_alemao = translate_text(textos, 'de')
    translate_alemao_text.config(text=traducao_alemao)

    translate_italiano_label.config(text="Italiano")
    checkbox_italiano.grid(row=6, column=5, padx=(10,0), pady=0, sticky=tk.W)
    traducao_italiano = translate_text(textos, 'it')
    translate_italiano_text.config(text=traducao_italiano)

