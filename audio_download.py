import os
import tkinter as tk
from tkinter import messagebox
from elevenlabs import save, Voice, VoiceSettings
from elevenlabs.client import *

# be00df312290494f3d432b0af6f9bc6c
# Oi, tudo bem com você? Baixe, e aproveite! É grátis.

# Função para converter texto para áudio utilizando Eleven Labs e salvar no desktop
def eleven(api, texto, save_filename, voice_name="James"):
    
    
    if not api:
        print("Por favor, insira a API do Elevenlabs.")
        return

    
    client = ElevenLabs(api_key=api)
    
    

    # Escolhe a voz baseada no nome fornecido
    voice = None
    voices = client.voices.get_all()
    for voz in voices.voices:
        if voice_name in voz.name:
            voice = voz.voice_id
            break

    if not voice:
        print(f"Voz '{voice_name}' não encontrada.")
        return

    # Configurações opcionais
    stability = 0.5
    similarity_boost = 0.8
    style = 0
    boost = True

    # Configurações opcionais original
    #stability = 0.35
    #similarity_boost = 0.4
    #style = 0.55
    #boost = False

    # Gera o áudio com a API do Eleven Labs
    audio = client.generate(
        text=texto,
        voice=Voice(voice_id=voice,
                    settings=VoiceSettings(stability=stability,
                                           similarity_boost=similarity_boost,
                                           style=style,
                                           use_speaker_boost=boost)),
        model='eleven_multilingual_v2'
    )

    # Salva o áudio em um arquivo com o nome fornecido
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    audios_folder = os.path.join(desktop_path, "idiomas")  # Pasta "idiomas" mencionada
    os.makedirs(audios_folder, exist_ok=True)
    filename = os.path.join(audios_folder, save_filename)

    save(audio=audio, filename=filename)
    print(f"Áudio salvo com sucesso como {filename}")
    
    
"""def criar_pasta_idiomas():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    idiomas_path = os.path.join(desktop_path, 'idiomas')
    if not os.path.exists(idiomas_path):
        os.makedirs(idiomas_path)
    return idiomas_path    """
      
    
    

# Função para baixar arquivos de áudio com base nos idiomas selecionados
"""def baixar_audio(api, pt):
    # Verifica se foi fornecida uma API válida
    if not api:
        print("Por favor, insira a API do Elevenlabs.")
        return

    idiomas_path = criar_pasta_idiomas()
    
    convert_text_to_audio(api_key=api, text=pt, save_filename="portuguese.mp3")"""
    
def baixa_audio(api_input, translate_portugues, translate_portugues_text, translate_portugues_label,
                translate_ingles, translate_ingles_text, translate_ingles_label,
                translate_espanhol, translate_espanhol_text, translate_espanhol_label,
                translate_frances, translate_frances_text, translate_frances_label,
                translate_alemao, translate_alemao_text, translate_alemao_label,
                translate_italiano, translate_italiano_text, translate_italiano_label,
                translate_arabe, translate_arabe_text, translate_arabe_label,
                translate_holandes, translate_holandes_text, translate_holandes_label,
                translate_polones, translate_polones_text, translate_polones_label,
                translate_bulgaro, translate_bulgaro_text, translate_bulgaro_label,
                translate_croata, translate_croata_text, translate_croata_label,
                translate_esloveno, translate_esloveno_text, translate_esloveno_label,
                translate_eslovaco, translate_eslovaco_text, translate_eslovaco_label,
                translate_filipino, translate_filipino_text, translate_filipino_label,
                translate_grego, translate_grego_text, translate_grego_label,
                translate_urdu, translate_urdu_text, translate_urdu_label,
                translate_lituano, translate_lituano_text, translate_lituano_label,
                translate_tailandes, translate_tailandes_text, translate_tailandes_label,
                translate_hindi, translate_hindi_text, translate_hindi_label,
                translate_vietnam, translate_vietnam_text, translate_vietnam_label,
                translate_bengali, translate_bengali_text, translate_bengali_label,
                translate_hungaro, translate_hungaro_text, translate_hungaro_label,
                translate_indonesio, translate_indonesio_text, translate_indonesio_label,
                translate_sueco, translate_sueco_text, translate_sueco_label,
                translate_servio, translate_servio_text, translate_servio_label,
                translate_tcheco, translate_tcheco_text, translate_tcheco_label,
                translate_romeno, translate_romeno_text, translate_romeno_label,
                translate_turco, translate_turco_text, translate_turco_label,
                translate_russo, translate_russo_text, translate_russo_label,
                translate_ucraniano, translate_ucraniano_text, translate_ucraniano_label,
                translate_malaio, translate_malaio_text, translate_malaio_label):
 
 # Obtém a API inserida pelo usuário
    api = api_input.get("1.0", tk.END).strip()
    resposta = messagebox.askquestion("Confirmação", "Deseja realmente baixar Áudios?")
    if resposta == "yes":      
        # Verifica se foi fornecida uma API válida
        if not api:
            messagebox.showerror("Erro", "Por favor, insira uma API válida.")
            return
    
        # Cria uma estrutura de dados para mapear cada idioma com seu texto e label associados
        languages_data = {
            "Português": (translate_portugues, translate_portugues_text, translate_portugues_label),
            "Inglês": (translate_ingles, translate_ingles_text, translate_ingles_label),
            "Espanhol": (translate_espanhol, translate_espanhol_text, translate_espanhol_label),
            "Francês": (translate_frances, translate_frances_text, translate_frances_label),
            "Alemão": (translate_alemao, translate_alemao_text, translate_alemao_label),
            "Italiano": (translate_italiano, translate_italiano_text, translate_italiano_label),
            "Árabe": (translate_arabe, translate_arabe_text, translate_arabe_label),
            "Holandês": (translate_holandes, translate_holandes_text, translate_holandes_label),
            "Polonês": (translate_polones, translate_polones_text, translate_polones_label),
            "Búlgaro": (translate_bulgaro, translate_bulgaro_text, translate_bulgaro_label),
            "Croata": (translate_croata, translate_croata_text, translate_croata_label),
            "Esloveno": (translate_esloveno, translate_esloveno_text, translate_esloveno_label),
            "Eslovaco": (translate_eslovaco, translate_eslovaco_text, translate_eslovaco_label),
            "Filipino": (translate_filipino, translate_filipino_text, translate_filipino_label),
            "Grego": (translate_grego, translate_grego_text, translate_grego_label),
            "Urdu": (translate_urdu, translate_urdu_text, translate_urdu_label),
            "Lituano": (translate_lituano, translate_lituano_text, translate_lituano_label),
            "Tailandês": (translate_tailandes, translate_tailandes_text, translate_tailandes_label),
            "Híndi": (translate_hindi, translate_hindi_text, translate_hindi_label),
            "Vietnamita": (translate_vietnam, translate_vietnam_text, translate_vietnam_label),
            "Bengali": (translate_bengali, translate_bengali_text, translate_bengali_label),
            "Húngaro": (translate_hungaro, translate_hungaro_text, translate_hungaro_label),
            "Indonésio": (translate_indonesio, translate_indonesio_text, translate_indonesio_label),
            "Sueco": (translate_sueco, translate_sueco_text, translate_sueco_label),
            "Sérvio": (translate_servio, translate_servio_text, translate_servio_label),
            "Tcheco": (translate_tcheco, translate_tcheco_text, translate_tcheco_label),
            "Romeno": (translate_romeno, translate_romeno_text, translate_romeno_label),
            "Turco": (translate_turco, translate_turco_text, translate_turco_label),
            "Russo": (translate_russo, translate_russo_text, translate_russo_label),
            "Ucraniano": (translate_ucraniano, translate_ucraniano_text, translate_ucraniano_label),
            "Malaio": (translate_malaio, translate_malaio_text, translate_malaio_label)
        }
    
        # Para cada idioma selecionado, verifica se está marcado e, se sim, realiza o download do áudio
        for language in languages_data:
            checkbox, text, label = languages_data.get(language, (None, None, None))
            if checkbox and checkbox.get():
                text_value = text.cget("text")
                save_filename = label.cget("text").strip() + ".mp3"
                eleven(api, text_value, save_filename)
        messagebox.showinfo("Download concluído", "Todos os downloads foram concluídos com sucesso.")

           
    else:
        # Caso o usuário clique em "Não", você pode optar por não fazer nada ou exibir uma mensagem
        print("Operação cancelada pelo usuário")
