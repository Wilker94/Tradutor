from deep_translator import GoogleTranslator
import tkinter as tk


#Wonka1 be00df312290494f3d432b0af6f9bc6c

def traduz_texto(texto_traducao_input, checkbox_portugues, translate_portugues_label, translate_portugues_text, 
                 checkbox_ingles, translate_ingles_label, translate_ingles_text, checkbox_espanhol, translate_espanhol_label, translate_espanhol_text, 
                 checkbox_frances, translate_frances_label, translate_frances_text, checkbox_alemao, translate_alemao_label, translate_alemao_text,
                 checkbox_italiano, translate_italiano_label, translate_italiano_text, checkbox_arabe, translate_arabe_label, translate_arabe_text,
                 checkbox_holandes, translate_holandes_label, translate_holandes_text, checkbox_polones, translate_polones_label, translate_polones_text, 
                 checkbox_bulgaro, translate_bulgaro_label, translate_bulgaro_text, checkbox_croata, translate_croata_label, translate_croata_text,
                 checkbox_esloveno, translate_esloveno_label, translate_esloveno_text, checkbox_eslovaco, translate_eslovaco_label, translate_eslovaco_text,
                 checkbox_filipino, translate_filipino_label, translate_filipino_text, checkbox_grego, translate_grego_label, translate_grego_text,
                 checkbox_lituano, translate_lituano_label, translate_lituano_text, checkbox_tailandes, translate_tailandes_label, translate_tailandes_text, 
                 checkbox_vietnam, translate_vietnam_label, translate_vietnam_text, checkbox_bengali, translate_bengali_label, translate_bengali_text,
                 checkbox_hungaro, translate_hungaro_label, translate_hungaro_text, checkbox_indonesio, translate_indonesio_label, translate_indonesio_text,
                 checkbox_sueco, translate_sueco_label, translate_sueco_text, checkbox_servio, translate_servio_label, translate_servio_text,
                 checkbox_tcheco, translate_tcheco_label, translate_tcheco_text, checkbox_romeno, translate_romeno_label, translate_romeno_text,
                 checkbox_turco, translate_turco_label, translate_turco_text, checkbox_russo, translate_russo_label, translate_russo_text,
                 checkbox_ucraniano, translate_ucraniano_label, translate_ucraniano_text, checkbox_malaio, translate_malaio_label, translate_malaio_text,
                 checkbox_urdu, translate_urdu_label, translate_urdu_text, checkbox_hindi, translate_hindi_label, translate_hindi_text):
       
        
    textos = texto_traducao_input.get("1.0", tk.END)  # Obtém o texto digitado na ScrolledText       
    
    translate_portugues_label.config(text="Português")
    checkbox_portugues.grid(row=6, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translate_portugues_text.config(text=textos)

    #Inglês en               
    translate_ingles_label.config(text="Inglês")
    checkbox_ingles.grid(row=6, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='en')
    translation = translator.translate(textos)
    translate_ingles_text.config(text=translation)
    
    #Espanhol es
    translate_espanhol_label.config(text="Espanhol")
    checkbox_espanhol.grid(row=6, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='es')
    translation = translator.translate(textos)
    translate_espanhol_text.config(text=translation)
        
    #frances fr
    translate_frances_label.config(text="Francês")
    checkbox_frances.grid(row=6, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='fr')
    translation = translator.translate(textos)
    translate_frances_text.config(text=translation)
    
    #alemão de        
    translate_alemao_label.config(text="Alemão")
    checkbox_alemao.grid(row=6, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='de')
    translation = translator.translate(textos)
    translate_alemao_text.config(text=translation)

    #Italiano it
    translate_italiano_label.config(text="Italiano")
    checkbox_italiano.grid(row=6, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='it')
    translation = translator.translate(textos)
    translate_italiano_text.config(text=translation)

    #Árabe AR
    translate_arabe_label.config(text="Árabe")
    checkbox_arabe.grid(row=8, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ar')
    translation = translator.translate(textos)
    translate_arabe_text.config(text=translation)
    
    #Holandes NL
    translate_holandes_label.config(text="Holandês")
    checkbox_holandes.grid(row=8, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='nl')
    translation = translator.translate(textos)
    translate_holandes_text.config(text=translation)
        
    #Polones PL
    translate_polones_label.config(text="Polonês")
    checkbox_polones.grid(row=8, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='pl')
    translation = translator.translate(textos)
    translate_polones_text.config(text=translation)
    
    #Búlgaro BG        
    translate_bulgaro_label.config(text="Búlgaro")
    checkbox_bulgaro.grid(row=8, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='bg')
    translation = translator.translate(textos)
    translate_bulgaro_text.config(text=translation)

    #Croata HR
    translate_croata_label.config(text="Croata")
    checkbox_croata.grid(row=8, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='hr')
    translation = translator.translate(textos)
    translate_croata_text.config(text=translation)

    #Esloveno SL
    translate_esloveno_label.config(text="Esloveno")
    checkbox_esloveno.grid(row=8, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='sl')
    translation = translator.translate(textos)
    translate_esloveno_text.config(text=translation)
    
    # Eslovaco
    translate_eslovaco_label.config(text="Eslovaco")
    checkbox_eslovaco.grid(row=10, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='sk')
    translation = translator.translate(textos)
    translate_eslovaco_text.config(text=translation)
    
    # Filipino (Tagalo)
    translate_filipino_label.config(text="Filipino")
    checkbox_filipino.grid(row=10, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='tl')
    translation = translator.translate(textos)
    translate_filipino_text.config(text=translation)
    
    # Grego
    translate_grego_label.config(text="Grego")
    checkbox_grego.grid(row=10, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='el')
    translation = translator.translate(textos)
    translate_grego_text.config(text=translation)
    
    """# Hebraico
    translate_hebraico_label.config(text="Hebraico")
    checkbox_hebraico.grid(row=10, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='he')
    translation = translator.translate(textos)
    translate_hebraico_text.config(text=translation)"""
    
    # Urdu
    translate_urdu_label.config(text="Urdu")
    checkbox_urdu.grid(row=10, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ur')
    translation = translator.translate(textos)
    translate_urdu_text.config(text=translation)
    
    # Lituano
    translate_lituano_label.config(text="Lituano")
    checkbox_lituano.grid(row=10, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='lt')
    translation = translator.translate(textos)
    translate_lituano_text.config(text=translation)
    
    # Tailandês
    translate_tailandes_label.config(text="Tailandês")
    checkbox_tailandes.grid(row=10, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='th')
    translation = translator.translate(textos)
    translate_tailandes_text.config(text=translation)
    
    # Chinês
    """translate_chines_label.config(text="Chinês")
    checkbox_chines.grid(row=12, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='zh')
    translation = translator.translate(textos)
    translate_chines_text.config(text=translation)"""
    
    # Híndi
    translate_hindi_label.config(text="Híndi")
    checkbox_hindi.grid(row=12, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='hi')
    translation = translator.translate(textos)
    translate_hindi_text.config(text=translation)
    
    # Vietnamita
    translate_vietnam_label.config(text="Vietnamita")
    checkbox_vietnam.grid(row=12, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='vi')
    translation = translator.translate(textos)
    translate_vietnam_text.config(text=translation)
    
    # Bengali
    translate_bengali_label.config(text="Bengali")
    checkbox_bengali.grid(row=12, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='bn')
    translation = translator.translate(textos)
    translate_bengali_text.config(text=translation)
    
    # Húngaro
    translate_hungaro_label.config(text="Húngaro")
    checkbox_hungaro.grid(row=12, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='hu')
    translation = translator.translate(textos)
    translate_hungaro_text.config(text=translation)
    
    # Indonésio
    translate_indonesio_label.config(text="Indonésio")
    checkbox_indonesio.grid(row=12, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='id')
    translation = translator.translate(textos)
    translate_indonesio_text.config(text=translation)
    
    # Sueco
    translate_sueco_label.config(text="Sueco")
    checkbox_sueco.grid(row=12, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='sv')
    translation = translator.translate(textos)
    translate_sueco_text.config(text=translation)
    
    # Sérvio
    translate_servio_label.config(text="Sérvio")
    checkbox_servio.grid(row=14, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='sr')
    translation = translator.translate(textos)
    translate_servio_text.config(text=translation)
    
    # Tcheco
    translate_tcheco_label.config(text="Tcheco")
    checkbox_tcheco.grid(row=14, column=2, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='cs')
    translation = translator.translate(textos)
    translate_tcheco_text.config(text=translation)
    
    # Romeno
    translate_romeno_label.config(text="Romeno")
    checkbox_romeno.grid(row=14, column=4, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ro')
    translation = translator.translate(textos)
    translate_romeno_text.config(text=translation)
    
    # Turco
    translate_turco_label.config(text="Turco")
    checkbox_turco.grid(row=14, column=6, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='tr')
    translation = translator.translate(textos)
    translate_turco_text.config(text=translation)
    
    # Russo
    translate_russo_label.config(text="Russo")
    checkbox_russo.grid(row=14, column=8, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ru')
    translation = translator.translate(textos)
    translate_russo_text.config(text=translation)
    
    # Ucraniano
    translate_ucraniano_label.config(text="Ucraniano")
    checkbox_ucraniano.grid(row=14, column=10, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='uk')
    translation = translator.translate(textos)
    translate_ucraniano_text.config(text=translation)
    
    # Malaio
    translate_malaio_label.config(text="Malaio")
    checkbox_malaio.grid(row=16, column=0, padx=(10,0), pady=0, sticky=tk.W)
    translator = GoogleTranslator(source='auto', target='ms')
    translation = translator.translate(textos)
    translate_malaio_text.config(text=translation)
    

    

