# Standard module imports
from Tkinter import *

# External module imports
import constants
from rock_paper_scissors import rps


# Initialize the interface
FONT = ('Helvetica', 11)
r_p_s = Tk()
r_p_s.title("Rock-Paper-Scissors Battle")
r_p_s.geometry("600x300")
r_p_s.resizable(0, 0)


class RPS_Interface(Frame):
    """Build interface for rock-paper-scissors game"""

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.create_widgets()

    def append_to_list(self, num):
        constants.USER_SELECTIONS.append(num)
        append_to_list_label = Label(self, text=rps(constants.USER_SELECTIONS))
        append_to_list_label.grid(row=1)

    def create_widgets(self):
        button_rock = Button(self, text="ROCK", font=FONT, borderwidth=2,
                             command=lambda: self.append_to_list(constants.ROCK))
        button_rock.grid(row=0, column=0, sticky="NSEW")

        button_paper = Button(self, text="PAPER", font=FONT, borderwidth=2,
                              command=lambda: self.append_to_list(constants.PAPER))
        button_paper.grid(row=0, column=1, sticky="NSEW")

        button_scissors = Button(self, text="SCISSORS", font=FONT, borderwidth=2,
                                 command=lambda: self.append_to_list(constants.SCISSORS))
        button_scissors.grid(row=0, column=2, sticky="NSEW")


if __name__ == '__main__':
    application = RPS_Interface(r_p_s).grid()
    r_p_s.mainloop()
