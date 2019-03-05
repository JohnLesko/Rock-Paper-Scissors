import Tkinter as tk
import constants
from rock_paper_scissors import rps

FONT = ('Verdana', 12)


class RPS_Interface(tk.Tk):
    """Build interface for rock-paper-scissors game"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Rock-Paper-Scissors Battle")
        tk.Tk.geometry(self, "800x400")
        tk.Tk.resizable(self, 0, 0)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = MainPage(container, self)
        self.frames[MainPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="RPS Machine", font=FONT)
        label.pack(padx=10, pady=5)

        button_rock = tk.Button(self, text="ROCK", command=self.rock_butt)
        button_rock.pack(side="left", padx=2)
        button_paper = tk.Button(self, text="PAPER", command=self.paper_butt)
        button_paper.pack(side="left")
        button_scissors = tk.Button(self, text="SCISSORS", command=self.scissors_butt)
        button_scissors.pack(side="left")

    def rock_butt(self):
        constants.count.append('0')
        rock_label = tk.Label(self, text=constants.count)
        rock_label.pack()

    def paper_butt(self):
        paper_label = tk.Label(self, text="Hey whatsup bro, I am doing something.")
        paper_label.pack()

    def scissors_butt(self):
        scissors_label = tk.Label(self, text="Hey whatsup bro, I am doing something.")
        scissors_label.pack()


if __name__ == '__main__':
    rps = RPS_Interface()
    rps.mainloop()
