# Standard module imports
from Tkinter import *

# External module imports
import constants
from rock_paper_scissors import rps


# Initialize the interface
FONT = ('Helvetica', 11)
r_p_s = Tk()
r_p_s.title("Rock-Paper-Scissors Battle")
r_p_s.resizable(0, 0)


class RPSInterface(Frame):
    """Build interface for rock-paper-scissors game"""
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.create_widgets()

    def multiple_call(self, num):
        # constants.USER_SELECTIONS.append(num)
        # rps(constants.USER_SELECTIONS)
        if num == 1:
            constants.counter_win += 1
            win_count.set(constants.counter_win)
        elif num == 2:
            constants.counter_tie += 1
            tie_count.set(constants.counter_tie)
        else:
            constants.counter_loses += 1
            computer_win_count.set(constants.counter_loses)

    def create_widgets(self):
        global win_count
        global tie_count
        global computer_win_count

        win_count = StringVar()
        win_count.set("0")
        display_win = Label(self, font=FONT, justify=CENTER, textvariable=win_count)
        display_win.grid(row=0, column=0, sticky="NSEW")

        tie_count = StringVar()
        tie_count.set("0")
        display_tie = Label(self, font=FONT, justify=CENTER, textvariable=tie_count)
        display_tie.grid(row=0, column=1, sticky="NSEW")

        computer_win_count = StringVar()
        computer_win_count.set("0")
        display_lose = Label(self, font=FONT, justify=CENTER, textvariable=computer_win_count)
        display_lose.grid(row=0, column=2, sticky="NSEW")

        person_win = Label(self, font=FONT, justify=CENTER, text="You Win")
        person_win.grid(row=1, column=0, sticky="NSEW")

        tie = Label(self, font=FONT, justify=CENTER, text="Tie")
        tie.grid(row=1, column=1, sticky="NSEW")

        computer_win = Label(self, font=FONT, justify=CENTER, text="Computer Win")
        computer_win.grid(row=1, column=2, sticky="NSEW")

        blank_label = Label(self, font=FONT, justify=CENTER, text=" ")
        blank_label.grid(row=2, columnspan=3, sticky="NSEW")

        button_rock = Button(self, text="ROCK", font=FONT, borderwidth=1,
                             command=lambda: self.multiple_call(constants.ROCK))
        button_rock.grid(row=3, column=0, sticky="NSEW")

        button_paper = Button(self, text="PAPER", font=FONT, borderwidth=1,
                              command=lambda: self.multiple_call(constants.PAPER))
        button_paper.grid(row=3, column=1, sticky="NSEW")

        button_scissors = Button(self, text="SCISSORS", font=FONT, borderwidth=1,
                                 command=lambda: self.multiple_call(constants.SCISSORS))
        button_scissors.grid(row=3, column=2, sticky="NSEW")

        blank_label = Label(self, font=FONT, justify=CENTER, text=" ")
        blank_label.grid(row=4, columnspan=3, sticky="NSEW")

        previous_game = Label(self, font=FONT, justify=CENTER, text="Previous Game Choices")
        previous_game.grid(row=5, columnspan=3, sticky="NSEW")

        previous_person = Label(self, justify=RIGHT, text="Your previous choice:")
        previous_person.grid(row=6, column=0)

        previous_computer = Label(self, justify=RIGHT, text="Computer previous choice:")
        previous_computer.grid(row=7, column=0)


if __name__ == '__main__':
    application = RPSInterface(r_p_s).grid()
    r_p_s.mainloop()
