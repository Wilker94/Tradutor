import tkinter as tk
from tkinter import filedialog
import pygame

# Inicialize o mixer do pygame
pygame.mixer.init()

def play_audio():
    pygame.mixer.music.load(audio_file_path.get())
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

def pause_audio():
    pygame.mixer.music.pause()

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    audio_file_path.set(file_path)

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Reprodutor de Áudio")

audio_file_path = tk.StringVar()

tk.Label(root, text="Arquivo de Áudio:").pack()
tk.Entry(root, textvariable=audio_file_path, width=50).pack()
tk.Button(root, text="Procurar", command=browse_file).pack()

tk.Button(root, text="Tocar", command=play_audio).pack()
tk.Button(root, text="Pausar", command=pause_audio).pack()


root.mainloop()
