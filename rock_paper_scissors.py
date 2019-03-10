# Standard module imports
import pandas as pd
import random

# External module imports
import constants


def win_tie_loss(user_selection, computer_choice):
    """
    Rock-Paper-Scissors game logic
    """
    if user_selection == computer_choice:
        return 'TIE'
    elif (user_selection == "PAPER") and (computer_choice == "ROCK"):
        return 'WIN'
    elif (user_selection == "ROCK") and (computer_choice == "SCISSORS"):
        constants.counter_win += 1
        return win_count.set(constants.counter_win)
    elif (user_selection == "SCISSORS") and (computer_choice == "PAPER"):
        constants.counter_win += 1
        return win_count.set(constants.counter_win)
    else:
        return "LOSE"



def rps(user_prediction):
    """
    Rock-Paper-Scissors game logic
    """
    try:
        if 1 and 2 and 3 in user_prediction:
            if conditional_probability_calc(user_prediction) == 1:
                return "PAPER"
            elif conditional_probability_calc(user_prediction) == 2:
                return "SCISSORS"
            else:
                return "ROCK"
        elif 1 and 2 in user_prediction:
            if conditional_probability_calc(user_prediction) == 1:
                return "PAPER"
            else:
                return "SCISSORS"
        elif 2 and 3 in user_prediction:
            if conditional_probability_calc(user_prediction) == 2:
                return "SCISSORS"
            else:
                return "ROCK"
        elif 1 and 3 in user_prediction:
            if conditional_probability_calc(user_prediction) == 1:
                return "PAPER"
            else:
                return "ROCK"
        elif 1 in user_prediction:
            return "PAPER"
        elif 2 in user_prediction:
            return "SCISSORS"
        elif 3 in user_prediction:
            return "ROCK"
        else:
            return "1-2-3 NOT in the list"
    except ValueError:
        return "Whoops, you killed me!"


def conditional_probability_calc(prediction):
    """
    Convert predictions list to DataFrame and calculate the conditional
    probability of the next choice based on the most recent selection
    """

    if prediction[-1] == 1:
        for i, j in enumerate(prediction):
            if (j == 1) and (len(prediction) != i + 1):
                constants.CONDITIONAL_PROBABILITY_1.append(prediction[i + 1])
        next_choice_prob = pd.DataFrame(constants.CONDITIONAL_PROBABILITY_1, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    elif prediction[-1] == 2:
        for i, j in enumerate(prediction):
            if (j == 2) and (len(prediction) != i + 1):
                constants.CONDITIONAL_PROBABILITY_2.append(prediction[i + 1])
        next_choice_prob = pd.DataFrame(constants.CONDITIONAL_PROBABILITY_2, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    else:
        for i, j in enumerate(prediction):
            if (j == 3) and (len(prediction) != i + 1):
                constants.CONDITIONAL_PROBABILITY_3.append(prediction[i + 1])
        next_choice_prob = pd.DataFrame(constants.CONDITIONAL_PROBABILITY_3, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
