import Tkinter as tk


class Interface:
    """Build interface for rock-paper-scissors game"""
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        # Create window title
        master.title("ROCK PAPER SCISSORS MACHINE")

        # Create buttons
        self.button_rock = tk.Button(master, text="ROCK")
        self.button_rock.pack(side="left")
        self.button_rock = tk.Button(master, text="PAPER")
        self.button_rock.pack(side="left")
        self.button_rock = tk.Button(master, text="SCISSORS")
        self.button_rock.pack(side="left")


if __name__ == '__main__':
    root = tk.Tk()
    rps = Interface(root)
    root.mainloop()
