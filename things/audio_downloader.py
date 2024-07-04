# audio_downloader.py

from tkinter import messagebox

def download_audio(translated_text):
    # Aqui você pode implementar a lógica para baixar o áudio
    # Substitua esta parte com sua própria implementação
    if not translated_text:
        messagebox.showwarning("Aviso", "Por favor, primeiro traduza o texto para alemão.")
        return
    else:
        print(f"Baixando áudio para o texto traduzido: {translated_text}")
