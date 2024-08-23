    
import os
import tkinter as tk
from tkinter import messagebox
from elevenlabs import save, Voice, VoiceSettings
from elevenlabs.client import *
import json

def eleven(api, texto, save_filename, voice_system, stability_system, similarity_system, style_system, boost_system ):
    
    
    if not api:
        print("Por favor, insira a API do Elevenlabs.")
        return

    
    client = ElevenLabs(api_key=api)
    
    

    # Escolhe a voz baseada no nome fornecido
    voice = None
    voices = client.voices.get_all()
    for voz in voices.voices:
        if voice_system in voz.name:
            voice = voz.voice_id
            break

    if not voice:
        print(f"Voz '{voice_system}' não encontrada.")
        return
 
    """
    # Configurações Ideais
    stability = 0.5
    similarity_boost = 0.8
    style = 0
    boost = True"""

    # Configurações opcionais original
    #stability = 0.35
    #similarity_boost = 0.4
    #style = 0.55
    #boost = False

    # Gera o áudio com a API do Eleven Labs
    audio = client.generate(
        text=texto,
        voice=Voice(voice_id=voice,
                    settings=VoiceSettings(stability=stability_system,
                                           similarity_boost=similarity_system,
                                           style=style_system,
                                           use_speaker_boost=boost_system)),
        model='eleven_multilingual_v2'
    )

    # Salva o áudio em um arquivo com o nome fornecido
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    audios_folder = os.path.join(desktop_path, "idiomas")  # Pasta "idiomas" mencionada
    os.makedirs(audios_folder, exist_ok=True)
    filename = os.path.join(audios_folder, save_filename)

    save(audio=audio, filename=filename)
    
    print(f"Áudio salvo com sucesso como {filename}")
    print(voice_system, stability_system, similarity_system, style_system,boost_system )
    print()
    
        
def baixa_audio(api_input, translate_portugues, translate_portugues_text, translate_portugues_label):
 
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

        }
        
        with open('config.json', 'r') as file:
    
            config = json.load(file)

            voice_system = config.get('default_name')
            stability_system = config.get('stability')
            similarity_system = config.get('similarity_boost')
            style_system = config.get('style')
            boost_system = config.get('boost')
    
        # Para cada idioma selecionado, verifica se está marcado e, se sim, realiza o download do áudio
        for language in languages_data:
            checkbox, text, label = languages_data.get(language, (None, None, None))
            if checkbox and checkbox.get():
                text_value = text.cget("text")
                save_filename = label.cget("text").strip() + ".mp3"
                eleven(api, text_value, save_filename, voice_system,stability_system, similarity_system, style_system, boost_system )
        messagebox.showinfo("Download concluído", "Todos os downloads foram concluídos com sucesso.")

           
    else:
        # Caso o usuário clique em "Não", você pode optar por não fazer nada ou exibir uma mensagem
        print("Operação cancelada pelo usuário")

def imprime(api_input_value):
    print("API Input:", api_input_value)
    #print("Texto Tradução:", texto_traducao_value)

    


def previa_voz(api_input):
    
    api_input_value = api_input.get()
    #texto_traducao_value = texto_traducao_input.cget("text").strip()
    
    imprime(api_input_value)
    


