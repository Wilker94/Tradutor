import tkinter as tk

class CharacterCounter(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.characters = 0
        self.config(text=f"Caracteres: {self.characters}")

    def update_counter(self, text):
        self.characters = len(text)
        self.config(text=f"Caracteres: {self.characters}")

if __name__ == "__main__":
    root = tk.Tk()
    counter = CharacterCounter(root)
    counter.pack()
    root.mainloop()
