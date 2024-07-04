# audio_converter.py

import os
from elevenlabs import save, Voice, VoiceSettings
from elevenlabs.client import ElevenLabs
from translate import translate_text  # Importa a função de tradução

def convert_text_to_audio(api_key, text, save_filename="audio.mp3", voice_name="Rachel"):
    client = ElevenLabs(api_key=api_key)

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
    stability = 0.35
    similarity_boost = 0.4
    style = 0.55
    boost = False

    # Gera o áudio com a API do Eleven Labs
    audio = client.generate(
        text=text,
        voice=Voice(voice_id=voice,
                    settings=VoiceSettings(stability=stability,
                                           similarity_boost=similarity_boost,
                                           style=style,
                                           use_speaker_boost=boost)),
        model='eleven_multilingual_v2'
    )

    # Salva o áudio em um arquivo com o nome fornecido
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    audios_folder = os.path.join(desktop_path, "audio")
    os.makedirs(audios_folder, exist_ok=True)
    filename = os.path.join(audios_folder, save_filename)

    save(audio=audio, filename=filename)
    print(f"Áudio salvo com sucesso como {filename}")
